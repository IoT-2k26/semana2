# Call external libraries
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED, Servo, TonalBuzzer
from gpiozero.tones import Tone


# Variables de LEDS y Buzzer
LED_RED_LEFT = LED(17)
LED_GREEN_LEFT = LED(22)
LED_YELLOW_LEFT = LED(27)

LED_RED_RIGHT = LED(12)
LED_GREEN_RIGHT = LED(20)
LED_YELLOW_RIGHT = LED(16)

BUZZER = TonalBuzzer(24)


# Variables de Servo
SERVO_LEFT = Servo(
    18,
    min_pulse_width=0.5/1000,
    max_pulse_width=2.5/1000
)

SERVO_RIGHT = Servo(
    25,
    min_pulse_width=0.5/1000,
    max_pulse_width=2.5/1000
)


# Controlar ambos servos
def change_servo(direction):

    if direction == "left":
        SERVO_LEFT.max()
        SERVO_RIGHT.min()

    elif direction == "right":
        SERVO_LEFT.min()
        SERVO_RIGHT.max()


# 10 parpadeos de la luz amarilla
def yellow_change():

    for i in range(10):

        LED_YELLOW_LEFT.on()
        LED_YELLOW_RIGHT.on()

        BUZZER.play(Tone(midi=60))

        sleep(0.5)

        LED_YELLOW_LEFT.off()
        LED_YELLOW_RIGHT.off()

        BUZZER.stop()

        sleep(0.5)


# Limpiar todos los LEDs
def limpiar():

    LED_RED_LEFT.off()
    LED_GREEN_LEFT.off()
    LED_YELLOW_LEFT.off()

    LED_RED_RIGHT.off()
    LED_GREEN_RIGHT.off()
    LED_YELLOW_RIGHT.off()


# Ciclo principal
lighter = True

while lighter == True:

    # IZQUIERDA VERDE / DERECHA ROJO
    LED_RED_LEFT.off()
    LED_GREEN_LEFT.on()
    LED_YELLOW_LEFT.off()

    LED_RED_RIGHT.on()
    LED_GREEN_RIGHT.off()
    LED_YELLOW_RIGHT.off()

    change_servo("left")

    sleep(10)


    # AMARILLO: 10 PARPADEOS
    limpiar()
    yellow_change()


    # IZQUIERDA ROJO / DERECHA VERDE
    LED_RED_LEFT.on()
    LED_GREEN_LEFT.off()
    LED_YELLOW_LEFT.off()

    LED_RED_RIGHT.off()
    LED_GREEN_RIGHT.on()
    LED_YELLOW_RIGHT.off()

    change_servo("right")

    sleep(10)


    # AMARILLO: 10 PARPADEOS
    limpiar()
    yellow_change()