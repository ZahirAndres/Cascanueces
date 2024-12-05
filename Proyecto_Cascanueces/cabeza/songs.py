# songs.py

from machine import Pin, PWM
from time import sleep_ms

# Notas musicales y sus frecuencias
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
D5 = 587
E5 = 659
F5 = 698
G5 = 784
REST = 0

# Configuración del buzzer
buzzer = PWM(Pin(5))

def play_tone(freq, duration):
    if freq == 0:  # REST
        buzzer.duty(0)
    else:
        buzzer.freq(freq)
        buzzer.duty(512)  # 50% duty cycle
    sleep_ms(duration)
    buzzer.duty(0)
    sleep_ms(50)  # Pequeña pausa entre notas

# Jingle Bells (versión completa)
JINGLE_BELLS = [
    # Intro
    (E4, 250), (E4, 250), (E4, 500),
    (E4, 250), (E4, 250), (E4, 500),
    (E4, 250), (G4, 250), (C4, 250), (D4, 250),
    (E4, 1000),
    # Segunda parte
    (F4, 250), (F4, 250), (F4, 250), (F4, 250),
    (F4, 250), (E4, 250), (E4, 250), (E4, 250),
    (E4, 250), (D4, 250), (D4, 250), (E4, 250),
    (D4, 500), (G4, 500),
    # Estribillo
    (E4, 250), (E4, 250), (E4, 500),
    (E4, 250), (E4, 250), (E4, 500),
    (E4, 250), (G4, 250), (C4, 250), (D4, 250),
    (E4, 1000),
    # Final
    (F4, 250), (F4, 250), (F4, 250), (F4, 250),
    (F4, 250), (E4, 250), (E4, 250), (E4, 250),
    (G4, 250), (G4, 250), (F4, 250), (D4, 250),
    (C4, 1000),
]

# Silent Night (versión completa)
SILENT_NIGHT = [
    # Primera estrofa
    (G4, 500), (A4, 250), (G4, 250),
    (E4, 1000),
    (G4, 500), (A4, 250), (G4, 250),
    (E4, 1000),
    (D5, 500), (D5, 500),
    (B4, 1000),
    (C5, 500), (C5, 500),
    (G4, 1000),
    # Segunda parte
    (A4, 500), (A4, 500),
    (C5, 500), (B4, 500),
    (G4, 500), (A4, 250), (G4, 250),
    (E4, 1000),
    (A4, 500), (A4, 500),
    (C5, 500), (B4, 500),
    (G4, 500), (A4, 250), (G4, 250),
    (E4, 1000),
]

# We Wish You a Merry Christmas (versión completa)
MERRY_CHRISTMAS = [
    # Primera parte
    (C4, 250), (F4, 250), (F4, 250), (G4, 250),
    (F4, 250), (E4, 250), (D4, 250), (C4, 250),
    (C4, 250), (G4, 250), (G4, 250), (A4, 250),
    (G4, 250), (F4, 250), (E4, 250), (D4, 250),
    # Estribillo
    (C4, 250), (C4, 250), (D4, 500),
    (G4, 500), (E4, 500),
    (F4, 250), (F4, 250), (F4, 250), (F4, 250),
    (E4, 250), (E4, 250), (E4, 250), (E4, 250),
    # Final
    (D4, 250), (D4, 250), (E4, 250), (D4, 250),
    (C4, 1000),
]

# Rudolph the Red-Nosed Reindeer (Nueva canción)
RUDOLPH = [
    # Primera parte
    (G4, 250), (A4, 250), (G4, 250), (E4, 250),
    (C5, 500), (A4, 500),
    (G4, 250), (A4, 250), (G4, 250), (E4, 250),
    (D5, 1000),
    # Segunda parte
    (G4, 250), (G4, 250), (A4, 250), (G4, 250),
    (C5, 500), (B4, 500),
    (F4, 250), (G4, 250), (F4, 250), (D4, 250),
    (E4, 1000),
    # Estribillo
    (C5, 500), (C5, 500),
    (C5, 250), (B4, 250), (A4, 250), (G4, 250),
    (A4, 500), (B4, 500),
    (C5, 500), (A4, 500),
    # Final
    (G4, 250), (A4, 250), (G4, 250), (E4, 250),
    (C5, 500), (A4, 500),
    (G4, 250), (F4, 250), (E4, 250), (D4, 250),
    (C4, 1000),
]

SONGS = [JINGLE_BELLS, SILENT_NIGHT, MERRY_CHRISTMAS, RUDOLPH]
current_song = 0

def play_current_song():
    song = SONGS[current_song]
    for note, duration in song:
        play_tone(note, duration)

def next_song():
    global current_song
    current_song = (current_song + 1) % len(SONGS)
    return current_song
