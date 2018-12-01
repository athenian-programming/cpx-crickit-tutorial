import random
import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

def random_color():
    intensity = 20
    return (random.randint(0, intensity), random.randint(0, intensity), random.randint(0, intensity))


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
