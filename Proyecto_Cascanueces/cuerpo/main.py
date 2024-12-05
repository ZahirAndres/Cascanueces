from time import sleep, ticks_ms, ticks_diff
from machine import Pin
from dht import DHT11
import network
from umqtt.simple import MQTTClient
import _thread
from led_patterns import run_current_pattern, next_pattern, clear_strip
from hcsr04 import HCSR04

# Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_TEMP = "zarm/temp"
MQTT_TOPIC_MOTOR = "zarm/pasos"
MQTT_TOPIC_SENSOR = "zarm/sensor"
MQTT_TOPIC_LED = "zarm/led"
MQTT_PORT = 1883

# Declarar valores del sensor de distancia
sensor_distancia = HCSR04(trigger_pin=14, echo_pin=12, echo_timeout_us=40000)

# Declarar los pines del motor paso a paso
IN1 = Pin(32, Pin.OUT)
IN2 = Pin(33, Pin.OUT)
IN3 = Pin(25, Pin.OUT)
IN4 = Pin(26, Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

# Secuencias mejoradas para movimientos más notorios
sequence_derecha = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

sequence_izquierda = sequence_derecha[::-1]

def step_motor(sequence, delay, steps):
    direction = "DERECHA ➡️" if sequence == sequence_derecha else "IZQUIERDA ⬅️"
    print(f"🔄 INICIANDO MOVIMIENTO DEL MOTOR")
    print(f"   Dirección: {direction}")
    print(f"   Pasos a ejecutar: {steps}")
    print(f"   Velocidad (delay): {delay}ms")
    
    steps_completed = 0
    for _ in range(steps):
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
            sleep(delay)
        steps_completed += 1
        if steps_completed % 50 == 0:  # Mostrar progreso cada 50 pasos
            print(f"   Progreso: {steps_completed}/{steps} pasos completados")
    
    print(f"✅ MOVIMIENTO COMPLETADO")
    print(f"   Total pasos ejecutados: {steps}")
    print("------------------------")
# Crear sensor DHT11 en el pin 27
sensor_dht11 = DHT11(Pin(27))

# Variable para almacenar el tiempo de la última señal recibida
last_msg_time = 0
TIMEOUT_INTERVAL = 5000  # 5 segundos

# Variable para controlar el estado del motor
motor_running = False

def conectar_wifi():
    print("📡 Conectando a WiFi...", end="") 
    sta_if = network.WLAN(network.STA_IF) 
    sta_if.active(True) 
    sta_if.connect('UTNG_GUEST', 'R3d1nv1t4d0s#UT') 
    while not sta_if.isconnected(): 
        print(".", end="") 
        sleep(0.3) 
    print("\n✅ WiFi Conectada!") 
    print(f"   Dirección IP: {sta_if.ifconfig()[0]}")
    
def ejecutar_movimiento_motor(pasos): 
    global motor_running
    print("\n🎯 COMANDO DE MOVIMIENTO RECIBIDO") 
    print(f"   Pasos solicitados: {pasos}") 
    motor_running = False  # Detener el movimiento continuo
    if pasos > 0: 
        print("   Tipo: Movimiento hacia la derecha") 
        step_motor(sequence_derecha, 0.002, pasos)  # Reducir el delay a 0.002 para mayor velocidad
    else: 
        print("   Tipo: Movimiento hacia la izquierda") 
        step_motor(sequence_izquierda, 0.002, abs(pasos))  # Reducir el delay a 0.002 para mayor velocidad

def llegada_mensaje(topic, msg): 
    global last_msg_time 
    topic = topic.decode('utf-8') 
    msg = msg.decode('utf-8') 
    print(f"\n📨 MENSAJE MQTT RECIBIDO") 
    print(f"   Tópico: {topic}") 
    print(f"   Mensaje: {msg}")
    
    try: 
        if topic == MQTT_TOPIC_MOTOR: 
            pasos = int(msg) 
            ejecutar_movimiento_motor(pasos) 
            last_msg_time = ticks_ms() 
        elif topic == MQTT_TOPIC_LED: 
            if msg.lower() == "siguiente": 
                print("   Cambiando patrón de LEDs") 
                next_pattern() 
            elif msg.lower() == "apagar": 
                print("   Apagando LEDs") 
                clear_strip() 
    except Exception as e: 
        print(f"❌ Error al procesar el mensaje: {e}")

def subscribir(): 
    client = MQTTClient(MQTT_CLIENT_ID, 
                        MQTT_BROKER, port=MQTT_PORT, 
                        user=MQTT_USER, 
                        password=MQTT_PASSWORD, 
                        keepalive=0) 
    client.set_callback(llegada_mensaje) 
    client.connect() 
    client.subscribe(MQTT_TOPIC_MOTOR) 
    client.subscribe(MQTT_TOPIC_LED) 
    print(f"✅ Conectado a broker MQTT: {MQTT_BROKER}") 
    print(f"   Tópicos suscritos: {MQTT_TOPIC_MOTOR}, {MQTT_TOPIC_LED}") 
    return client

# Conectar a WiFi
conectar_wifi()

# Subscripción a un broker MQTT
client = subscribir()

# Hilo para manejar los patrones LED
def led_thread():
    while True:
        run_current_pattern()
        sleep(1)

# Iniciar hilo para patrones LED
_thread.start_new_thread(led_thread, ())

print("\n🚀 Sistema iniciado y listo para recibir comandos")
print("   Esperando mensajes MQTT...")

while True:
    try:
        client.check_msg()  # Check for new messages

        # Medir la distancia y enviar la lectura a través de MQTT
        distancia = sensor_distancia.distance_cm()
        client.publish(MQTT_TOPIC_SENSOR, str(distancia))
        
        # Medir la temperatura y humedad con el sensor DHT11
        sensor_dht11.measure()
        temperatura = sensor_dht11.temperature()
        humedad = sensor_dht11.humidity()
        
        # Publicar temperatura y humedad
        client.publish(MQTT_TOPIC_TEMP, f"Temp: {temperatura}°C Hum: {humedad}%")
        
        print(f"🌡️ Temperatura: {temperatura}°C Humedad: {humedad}% Distancia: {distancia}cm")
        
        # Verificar si ha pasado el tiempo de espera sin recibir un mensaje
        current_time = ticks_ms()
        if ticks_diff(current_time, last_msg_time) > TIMEOUT_INTERVAL:
            print("⚠️ Tiempo de espera excedido. Moviendo el motor.")
            motor_running = True

        # Si el motor debe estar funcionando, ejecuta un paso
        if motor_running:
            for step in sequence_derecha:
                for i in range(len(pins)):
                    pins[i].value(step[i])
                sleep(0.001)  # Reducir el delay a 0.001 para mayor velocidad

        # Esperar un segundo antes de la siguiente iteración
        sleep(1)
    except OSError as e:
        print(f"❌ Error en el bucle principal: {e}")
        try:
            # Intentar reconectar a MQTT en caso de fallo de conexión
            print("🔄 Reconectando a MQTT...")
            client = subscribir()  # Reconectar al broker MQTT
        except Exception as ex:
            print(f"❌ Error al reconectar a MQTT: {ex}")
            sleep(5)  # Esperar 5 segundos antes de reintentar		