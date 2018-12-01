import time

import board
from analogio import AnalogIn

# A2 is used here, but A1 and A3 are also candidates
analogin = AnalogIn(board.A2)

while True:
    voltage = analogin.value / 65536
    print((voltage,))
    time.sleep(0.1)
