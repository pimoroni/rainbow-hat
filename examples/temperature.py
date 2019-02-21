#!/usr/bin/env python
import time
import colorsys

import rainbowhat


RAINBOW_BRIGHTNESS = 255

HUE_COLD = 225
HUE_WARM = 0

T_COLD = 15
T_WARM = 30

print("""Displays the temperature on Rainbow HAT.

Press Ctrl+C or touch A to exit.

""")

running = True


@rainbowhat.touch.A.press()
def touch_a(channel):
    global running
    running = False


def set_rainbow(temp):
    temp = max(temp, T_COLD)
    temp = min(temp, T_WARM)

    temp -= T_COLD
    temp /= float(T_WARM - T_COLD)

    hue = (1.0 - temp) * abs(HUE_WARM - HUE_COLD) / 360.0

    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

    rainbowhat.rainbow.set_all(r, g, b, brightness=0.1)
    rainbowhat.rainbow.show()


try:
    while running:
        temperature = rainbowhat.weather.temperature()

        set_rainbow(temperature)

        rainbowhat.display.print_float(temperature)
        rainbowhat.display.show()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass


rainbowhat.display.clear()
rainbowhat.display.show()
