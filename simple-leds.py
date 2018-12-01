import random
import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
max_intensity = 20


def random_color():
    return (random.randint(0, max_intensity), random.randint(0, max_intensity), random.randint(0, max_intensity))


while True:
    # Clear the pixels
    pixels.fill((0, 0, 0))

    # Assign random colors to each LED
    for i in range(len(pixels)):
        pixels[i] = random_color()
        time.sleep(.1)

    time.sleep(1)

    # Assign random color to all LEDs
    pixels.fill(random_color())

    time.sleep(1)
