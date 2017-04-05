#!/usr/bin/env python

import random
import time

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_pixel=rainbowhat.rainbow.set_pixel
show=rainbowhat.rainbow.show

set_clear_on_exit()

while True:
    pixels = random.sample(range(7), random.randint(1, 5))
    for i in range(7):
        if i in pixels:
            set_pixel(i, 255, 150, 0)
        else:
            set_pixel(i, 0, 0, 0)
    show()
    time.sleep(0.05)
