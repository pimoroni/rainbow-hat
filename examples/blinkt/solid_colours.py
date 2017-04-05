#!/usr/bin/env python

import time

import rainbowhat

set_clear_on_exit=rainbowhat.rainbow.set_clear_on_exit
set_all=rainbowhat.rainbow.set_all
show=rainbowhat.rainbow.show

set_clear_on_exit()

step = 0

while True:
    if step == 0:
        set_all(128,0,0)
    if step == 1:
        set_all(0,128,0)
    if step == 2:
        set_all(0,0,128)

    step+=1
    step%=3
    show()
    time.sleep(0.5)
