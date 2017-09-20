#!/usr/bin/env python

import colorsys
import time

import rainbowhat

BRIGHTNESS = 0.1
A = 0
B = 1
C = 2

hue = 0

inputs = [False, False, False]

@rainbowhat.touch.press()
def touch_press(channel):
    global inputs
    inputs[channel] = True
    rainbowhat.lights[channel].on()

@rainbowhat.touch.release()
def touch_release(channel):
    global inputs
    inputs[channel] = False
    rainbowhat.lights[channel].off()

while True:
    if inputs[A]:
        hue -= 0.1
    if inputs[C]:
        hue += 0.1
    if inputs[B]:
        hue = 0

    hue %= 360
    rainbowhat.display.clear()
    rainbowhat.display.print_float(round(hue,1))
    rainbowhat.display.show()

    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
    rainbowhat.rainbow.set_all(r, g, b, brightness=BRIGHTNESS)
    rainbowhat.rainbow.show()
    time.sleep(0.001)
   
