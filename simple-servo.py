import time

from adafruit_crickit import crickit

crickit.servo_1.set_pulse_width_range(min_pulse=500, max_pulse=2500)

while True:
    for i in range(7):
        crickit.servo_1.angle = i * 30
        time.sleep(0.5)

    for i in range(5, 0, -1):
        crickit.servo_1.angle = i * 30
        time.sleep(0.5)
