# code from Learning Card 08 - Rainbow HAT

# import the rainbowhat and signal modules
import rainbowhat
import signal

# this section links a press on button A
# to what to do when it happens
@rainbowhat.touch.A.press()
def touch_a(channel):
    rainbowhat.lights.rgb(1, 0, 0)


# this section links a letting go of any button
# to what to do when it happens
@rainbowhat.touch.release()
def release(channel):
    rainbowhat.lights.rgb(0, 0, 0)

# waits until a signal is received
signal.pause()

