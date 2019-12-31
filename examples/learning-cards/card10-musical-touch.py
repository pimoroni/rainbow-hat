# code from Learning Card 10 - Rainbow HAT

# import the rainbowhat and signal modules
import rainbowhat
import signal

# this section links a press on button A
# to what to do when it happens
@rainbowhat.touch.A.press()
def touch_a(channel):

    # this time we make the buzzer sound
    # as well as making the button light come on
    rainbowhat.lights.rgb(1, 0, 0)
    rainbowhat.buzzer.midi_note(65, 1)

# add the same for button B
@rainbowhat.touch.B.press()
def touch_b(channel):
    rainbowhat.lights.rgb(0, 1, 0)
    rainbowhat.buzzer.midi_note(80, 1)

# this section links a letting go of any button
# to what to do when it happens
@rainbowhat.touch.release()
def release(channel):
    rainbowhat.lights.rgb(0, 0, 0)


# waits until a signal is received
signal.pause()
