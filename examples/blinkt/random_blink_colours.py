#!/usr/bin/env python

import random
import time

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_pixel=rainbowhat.rainbow.set_pixel
show=rainbowhat.rainbow.show
set_brightness=rainbowhat.rainbow.set_brightness

set_clear_on_exit()
set_brightness(0.1)

while True:
    for i in range(7):
        set_pixel(i, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    show()
    time.sleep(0.05)
