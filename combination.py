import time

import board
import neopixel
from adafruit_crickit import crickit
from analogio import AnalogIn

analogin = AnalogIn(board.A2)

crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

while True:
    voltage = analogin.value / 65536
    print((voltage,))

    led_val = (voltage * 9) - 0.05

    for i in range(len(pixels)):
        if i < led_val:
            pixels[i] = (0, 10, 0)
        else:
            pixels[i] = (0, 0, 0)

    servo_val = voltage * 180
    crickit.servo_1.angle = servo_val

    time.sleep(0.05)
