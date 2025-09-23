from machine import Pin
import time

pines = [2, 5, 18, 19, 21, 22, 23, 25]
leds = [Pin(pin, Pin.OUT) for pin in pines]

while True:
    for led in leds:
        led.value(1)
        time.sleep(1)
        led.value(0)

