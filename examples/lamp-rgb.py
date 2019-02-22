#!/usr/bin/env python

import time

import rainbowhat

print("""Lamp: RGB Edition

Control the colour of the rainbow by adjusting the Red, Green and Blue
channels separately.

Tap button A to pick which channel to adjust.

Tap button B to lower that colour's brightness.

Tap button C to raise that colour's brightness.

Press Ctrl+C to exit!

""")

BRIGHTNESS = 0.1
A = 0
B = 1
C = 2

values = [['R', 0], ['G', 0], ['B', 0]]

mode = 0

show = "RGB"

# Store the state of the inputs
inputs = [False, False, False]

# Store the speed to increment colour
speeds = [0, 1, 1]

# Introduce each button and its feature

rainbowhat.lights.rgb(1, 0, 0)
rainbowhat.display.print_str("Chan")
rainbowhat.display.show()
time.sleep(1.0)

rainbowhat.lights.rgb(0, 1, 0)
rainbowhat.display.print_str("Less")
rainbowhat.display.show()
time.sleep(1.0)

rainbowhat.lights.rgb(0, 0, 1)
rainbowhat.display.print_str("More")
rainbowhat.display.show()
time.sleep(1.0)

rainbowhat.lights.rgb(0, 0, 0)


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
        mode += 1
        mode %= 3
        rainbowhat.buzzer.note(880, 0.1)

    if inputs[B]:
        values[mode][1] -= int(speeds[B])
        speeds[B] += 0.5  # Ramp the speed up slightly
    else:
        speeds[B] = 1     # Reset speed if button is release

    if inputs[C]:
        values[mode][1] += int(speeds[C])
        speeds[C] += 0.5
    else:
        speeds[C] = 1

    # Clamp to 0 to 255
    if values[mode][1] > 255:
        values[mode][1] = 255

    if values[mode][1] < 0:
        rainbowhat.buzzer.note(440, 0.1)
        values[mode][1] = 0

    # Get the name and value of the current channel
    name, value = values[mode]
    show = "{name}{value}".format(name=name, value=value)

    # Grab the rgb values from the values list
    r, g, b = [x[1] for x in values]

    rainbowhat.display.clear()
    rainbowhat.display.print_str(show, justify_right=False)
    rainbowhat.display.show()

    rainbowhat.rainbow.set_all(r, g, b, brightness=BRIGHTNESS)
    rainbowhat.rainbow.show()

    if inputs[A]:  # Add a slight delay to prevent flipping through mode too quickly
        time.sleep(0.5)
    else:
        time.sleep(0.1)
