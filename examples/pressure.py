#!/usr/bin/env python
import time
import colorsys

import rainbowhat


RAINBOW_BRIGHTNESS = 255

HUE_LOW = 225
HUE_HIGH = 0

P_LOW = 900
P_HIGH = 1100

print("""Displays the pressure on Rainbow HAT.

Press Ctrl+C or touch A to exit.

""")

running = True

@rainbowhat.touch.A.press()
def touch_a(channel):
    global running
    running = False

def set_rainbow(temp):
    temp = max(temp,P_LOW)
    temp = min(temp,P_HIGH)

    temp -= P_LOW
    temp /= float(P_HIGH - P_LOW)

    hue = (1.0-temp) * abs(HUE_HIGH - HUE_LOW) / 360.0

    r, g, b = [int(c * 255) for c in  colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

    rainbowhat.rainbow.set_all(r, g, b, brightness=0.1)
    rainbowhat.rainbow.show()


try:
    while running:
        pressure = rainbowhat.weather.pressure()

        set_rainbow(pressure)

        rainbowhat.display.print_float(pressure)
        rainbowhat.display.show()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass


rainbowhat.display.clear()
rainbowhat.display.show()
