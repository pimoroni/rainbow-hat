#!/usr/bin/env python

import colorsys
import time

import rainbowhat

BRIGHTNESS = 0.1
A = 0
B = 1
C = 2

r, g, b = (0, 0, 0)
show = "RGB"

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
        r += 1
        show = "R{}".format(r)

    if inputs[B]:
        g += 1
        show = "G{}".format(g)

    if inputs[C]:
        b += 1
        show = "B{}".format(b)

    r, g, b = [x % 255 for x in (r, g, b)]

    rainbowhat.display.clear()
    rainbowhat.display.print_str(show, justify_right=False)
    rainbowhat.display.show()

    rainbowhat.rainbow.set_all(r, g, b, brightness=BRIGHTNESS)
    rainbowhat.rainbow.show()

    time.sleep(0.05)
   
