import random
import time

import board
import neopixel
from adafruit_crickit import crickit
from analogio import AnalogIn

RED = (10, 0, 0)
BLUE = (0, 10, 0)
GREEN = (0, 0, 10)
color = RED

analogin = AnalogIn(board.A2)

crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)


def random_color():
    intensity = 20
    return (random.randint(0, intensity), random.randint(0, intensity), random.randint(0, intensity))

while True:
    voltage = analogin.value / 65536
    print((voltage,))

    led_val = (voltage * 9) - 0.05
    for i in range(len(pixels)):
        if i < led_val:
            pixels[i] = color
        else:
            pixels[i] = (0, 0, 0)

    crickit.servo_1.angle = voltage * 180

    if crickit.touch_1.value:
        color = RED
    if crickit.touch_2.value:
        color = BLUE
    if crickit.touch_3.value:
        color = GREEN
    if crickit.touch_4.value:
        color = random_color()


    time.sleep(0.05)
