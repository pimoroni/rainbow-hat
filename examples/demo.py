#!/usr/bin/env python

import colorsys
import time

import rainbowhat

notes = [
    71,   71,   71,   71,   71,  71, 71, 64, 67, 71,
    69,   69,   69,   69,   69,  69, 69, 62, 66, 69,
    71,   71,   71,   71,   71,  71, 71, 73, 74, 77,
    74,   71,   69,   66,   64,  64
]
times = [
    300,  50,   50,   300, 50, 50, 300, 300, 300, 200,
    300,  50,   50,   300, 50, 50, 300, 300, 300, 200,
    300,  50,   50,   300, 50, 50, 300, 300, 300, 200,
    300,  300,  300,  300, 600, 600
]

def display_message(message):
    rainbowhat.display.print_str(message)
    rainbowhat.display.show()

@rainbowhat.touch.A.press()
def press_a(channel):
    display_message("AHOY")
    rainbowhat.lights.rgb(1,0,0)

@rainbowhat.touch.B.press()
def press_b(channel):
    display_message("YARR")
    rainbowhat.lights.rgb(0,1,0)

@rainbowhat.touch.C.press()
def press_c(channel):
    display_message("GROG")
    rainbowhat.lights.rgb(0,0,1)

note_index = 0

current_time = 0
last_time = time.time()

display_message("WJDK")

try:
    while True:
        if time.time() > last_time + current_time:
            current_note = notes[note_index]
            current_time = times[note_index] / 1000.0
            current_time += 0.1
            note_index += 1
            note_index %= len(notes)
            last_time = time.time()
            if current_note == 128 or current_time == 0:
                pass
                #rainbowhat.buzzer.stop()
                #print("Note Off")
            else:
                rainbowhat.buzzer.midi_note(current_note, current_time*0.9)
                #print("Playing Note: {}".format(current_note))

        for x in range(7):
            delta = time.time() * 20
            hue = delta + (x*10)
            hue %= 360 # Clamp to 0-359.9r
            hue /= 360.0 # Scale to 0.0 to 1.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
            rainbowhat.rainbow.set_pixel(6-x, r, g, b, brightness=0.1)

        rainbowhat.rainbow.show()
        time.sleep(0.05)

except KeyboardInterrupt:
    pass
