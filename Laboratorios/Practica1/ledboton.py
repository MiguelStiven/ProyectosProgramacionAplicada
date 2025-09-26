from machine import Pin
import time

boton = Pin(16, Pin.IN, Pin.PULL_UP)
pines = [2, 4, 17, 18, 19, 21, 22, 23, 25]
leds = [Pin(pin_num, Pin.OUT) for pin_num in pines]

boton_anterior = 1
led_count = 0
encendiendo = True

while True:
    boton_actual = boton.value()
    if boton_anterior == 1 and boton_actual == 0:
        if encendiendo:
            led_count += 1
            if led_count > len(leds):
                led_count = len(leds)
                encendiendo = False
        else:
            led_count -= 1
            if led_count < 0:
                led_count = 0
                encendiendo = True
        for i, led in enumerate(leds):
            led.value(1 if i < led_count else 0)
        time.sleep(0.2)
    boton_anterior = boton_actual
    time.sleep(0.01)
