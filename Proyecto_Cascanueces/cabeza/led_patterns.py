from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

# Configuración de la tira LED
LED_PIN = 27  # Pin para la tira LED
NUM_LEDS = 43  # Número de LEDs en la tira
np = NeoPixel(Pin(LED_PIN), NUM_LEDS)

# Colores predefinidos
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def clear_strip():
    np.fill(OFF)
    np.write()

# Patrón 1: Efecto cascada navideño
def patron_cascada():
    colors = [RED, GREEN, WHITE]  # Colores navideños
    for i in range(NUM_LEDS):
        np[i] = colors[i % 3]
        np.write()
        sleep_ms(50)
    sleep_ms(500)

# Patrón 2: Parpadeo alternado
def patron_parpadeo():
    for _ in range(5):  # 5 ciclos de parpadeo
        # Enciende LEDs pares
        for i in range(0, NUM_LEDS, 2):
            np[i] = RED
            if i + 1 < NUM_LEDS:
                np[i + 1] = OFF
        np.write()
        sleep_ms(500)
        
        # Enciende LEDs impares
        for i in range(0, NUM_LEDS, 2):
            np[i] = OFF
            if i + 1 < NUM_LEDS:
                np[i + 1] = GREEN
        np.write()
        sleep_ms(500)

# Patrón 3: Efecto arcoíris móvil
def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

def patron_arcoiris():
    for j in range(256):
        for i in range(NUM_LEDS):
            np[i] = wheel(((i * 256 // NUM_LEDS) + j) & 255)
        np.write()
        sleep_ms(20)

# Lista de patrones disponibles
PATTERNS = [patron_cascada, patron_parpadeo, patron_arcoiris]
current_pattern = 0

def run_current_pattern():
    clear_strip()
    PATTERNS[current_pattern]()

def next_pattern():
    global current_pattern
    current_pattern = (current_pattern + 1) % len(PATTERNS)
    return current_pattern
