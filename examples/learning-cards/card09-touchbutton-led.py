# code from Learning Card 09 - Rainbow HAT

# import the rainbowhat and signal modules
import rainbowhat
import signal

# this section links a press on button A
# to what to do when it happens
@rainbowhat.touch.A.press()
def touch_a(channel):

    # this time we make the rainbow leds come on
    # as well as the button light
    rainbowhat.lights.rgb(1, 0, 0)
    rainbowhat.rainbow.set_pixel(3, 0, 255, 0, 0.1)
    rainbowhat.rainbow.show()


# this section links a letting go of any button
# to what to do when it happens
@rainbowhat.touch.release()
def release(channel):

    # turn the button light off, and also
    # turn the rainbow led off
    rainbowhat.lights.rgb(0, 0, 0)
    rainbowhat.rainbow.set_pixel(3, 0, 255, 0, 0.1)
    rainbowhat.rainbow.show()


# waits until a signal is received
signal.pause()
