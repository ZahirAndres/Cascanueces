import network
from umqtt.simple import MQTTClient
from machine import Pin, PWM, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep
from songs import play_current_song, next_song
from eye import draw_both_eyes, blink
import _thread

# Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""  # Cambia esto a un ID único para tu cliente MQTT
MQTT_TOPIC_MUSIC = "zarm/musica"  # Tópico para control de música
MQTT_TOPIC_SERVO = "zarm/servo"  # Tópico para control del servo
MQTT_PORT = 1883

# Inicializar I2C y OLED displays con SoftI2C para ambos displays
# Primer OLED display (ojo izquierdo)
i2c1 = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
oled1 = SSD1306_I2C(128, 64, i2c1)

# Segundo OLED display (ojo derecho)
i2c2 = SoftI2C(scl=Pin(19), sda=Pin(18), freq=100000)
oled2 = SSD1306_I2C(128, 64, i2c2)

# Configurar el servo en el pin 15
servo = PWM(Pin(15), freq=50)  # Frecuencia de 50Hz para servos

def mover_servo(angulo):
    """Convierte el ángulo a un valor de ciclo de trabajo (duty) adecuado para el servo"""
    if 0 <= angulo <= 180:
        # Mapeo del ángulo (0-180) al rango de duty (40-115)
        duty = int(40 + (angulo / 180) * 75)  # Mapea de 0-180 a 40-115
        servo.duty(duty)
        print(f"Servo movido a {angulo} grados.")
    else:
        print("Ángulo fuera de rango. Debe estar entre 0 y 180.")

def mover_servo_lento(angulo, velocidad=5):
    """Mueve el servo al ángulo deseado lentamente con la velocidad especificada."""
    if 0 <= angulo <= 180:
        # Obtener el ángulo actual del servo
        angulo_actual = servo.duty() - 40
        angulo_actual = int((angulo_actual / 75) * 180)
        
        if angulo_actual < angulo:
            for a in range(angulo_actual, angulo + 1, velocidad):
                duty = int(40 + (a / 180) * 75)
                servo.duty(duty)
                sleep(0.02)  # Ajustar el tiempo de espera según la suavidad deseada
        else:
            for a in range(angulo_actual, angulo - 1, -velocidad):
                duty = int(40 + (a / 180) * 75)
                servo.duty(duty)
                sleep(0.02)  # Ajustar el tiempo de espera según la suavidad deseada

        print(f"Servo movido a {angulo} grados lentamente.")
    else:
        print("Ángulo fuera de rango. Debe estar entre 0 y 180.")

# Conectar a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_GUEST', 'R3d1nv1t4d0s#UT')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")

# Función que se llama cuando llega un mensaje
def llegada_mensaje(topic, msg):
    topic = topic.decode('utf-8')
    msg = msg.decode('utf-8')
    print("Mensaje recibido en el tópico %s: %s" % (topic, msg))
    
    
    try:
        if topic == MQTT_TOPIC_SERVO:
            # Mensaje para controlar el servo
            if msg.lower() == "mover":
                mover_servo_lento(175)  # Mover el servo a 90 grados
            elif msg.lower() == "reset":
                mover_servo(0)  # Mover el servo a 0 grados
        elif topic == MQTT_TOPIC_MUSIC:
            # Mensaje para cambiar la música
            if msg.lower() == "siguiente":
                # Cambiar a la siguiente canción
                next_song()
                print(f"Reproduciendo siguiente canción")
    except Exception as e:
        print("Error al procesar el mensaje: ", e)

# Función para suscribirse al broker y tópico MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
                        MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER,
                        password=MQTT_PASSWORD,
                        keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC_MUSIC)
    client.subscribe(MQTT_TOPIC_SERVO)
    print("Conectado a %s, en los tópicos %s y %s" % 
          (MQTT_BROKER, MQTT_TOPIC_MUSIC, MQTT_TOPIC_SERVO))
    return client

# Testear los displays OLED
def test_displays():
    """Test both displays individually"""
    # Test first display
    oled1.fill(0)
    oled1.text("Right Eye", 20, 20)
    oled1.text("Testing...", 20, 35)
    oled1.show()
    
    sleep(2)
    
    # Test second display
    oled2.fill(0)
    oled2.text("Left Eye", 20, 20)
    oled2.text("Testing...", 20, 35)
    oled2.show()
    
    sleep(2)

# Animación de ojos
def animate_eyes():
    blink_counter = 0
    while True:
        # Look right together
        draw_both_eyes(oled1, oled2, 1, 0)
        sleep(1)
        
        # Blink in right position
        blink(oled1, oled2)
        sleep(0.5)
        
        # Back to center
        draw_both_eyes(oled1, oled2, 0, 0)
        sleep(1)
        
        # Random blink in center
        blink_counter += 1
        if blink_counter % 3 == 0:
            blink(oled1, oled2)
            sleep(0.5)

# Hilo para manejar la música
def music_thread():
    while True:
        play_current_song()
        sleep(1)

# Hilo para manejar la suscripción MQTT
def mqtt_thread():
    client = subscribir()
    while True:
        client.check_msg()  # Verificar mensajes MQTT
        sleep(1)

# Conectar a WiFi
conectar_wifi()

# Testear displays
test_displays()

# Iniciar hilos para animación de ojos, música y MQTT
_thread.start_new_thread(animate_eyes, ())
_thread.start_new_thread(music_thread, ())
_thread.start_new_thread(mqtt_thread, ())

# Ciclo principal (vacío, ya que los hilos están manejando las tareas)
while True:
    
    sleep(1)
