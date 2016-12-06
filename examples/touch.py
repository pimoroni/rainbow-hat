#!/usr/bin/env python

import signal

import rainbowhat


@rainbowhat.touch.A.press()
def touch_a(channel):
    print("Button A touched!")
    rainbowhat.lights.rgb(1,0,0)

@rainbowhat.touch.B.press()
def touch_b(channel):
    print("Button B touched!")
    rainbowhat.lights.rgb(0,1,0)

@rainbowhat.touch.C.press()
def touch_c(channel):
    print("Button C touched!")
    rainbowhat.lights.rgb(0,0,1)

@rainbowhat.touch.release()
def release(channel):
    print("Button release!")
    rainbowhat.lights.rgb(0,0,0)

signal.pause() # Pause the main thread so it doesn't exit
