#!/usr/bin/env python

import colorsys
import time

import rainbowhat


try:
    while True:
        for x in range(7):
            delta = time.time() * 20
            hue = delta + (x * 10)
            hue %= 360    # Clamp to 0-359.9r
            hue /= 360.0  # Scale to 0.0 to 1.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
            rainbowhat.rainbow.set_pixel(6 - x, r, g, b, brightness=0.1)

        rainbowhat.rainbow.show()
        time.sleep(0.05)

except KeyboardInterrupt:
    pass
