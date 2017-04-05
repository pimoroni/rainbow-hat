#!/usr/bin/env python

import colorsys
import math
import time

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_pixel=rainbowhat.rainbow.set_pixel
show=rainbowhat.rainbow.show
set_brightness=rainbowhat.rainbow.set_brightness

set_clear_on_exit()

hue_range = 120
hue_start = 0
max_brightness = 0.2

def show_graph(v, r, g, b):
    v *= 7
    for x in range(7):
        hue = ((hue_start + ((x/7.0) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue,1.0,1.0)]
        if v  < 0:
            brightness = 0
        else:
            brightness = min(v,1.0) * max_brightness
        set_pixel(x, r, g, b, brightness)
        v -= 1

    show()

set_brightness(0.1)

try:
    while True:
        t = time.time() * 2
        v = (math.sin(t) + 1) / 2 # Get a value between 0 and 1
        show_graph(v,255,0,255)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass
