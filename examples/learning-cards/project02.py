# import the rainbowhat and time modules
import rainbowhat
import time

# set the first LED to red, show it, and wait 1 second before continuing
rainbowhat.rainbow.set_pixel(6, 255, 0, 0, 0.1)
rainbowhat.rainbow.show()
time.sleep(1)

# set the second LED to orange, show it, and wait 1 second before continuing
rainbowhat.rainbow.set_pixel(5, 255, 100, 0, 0.1)
rainbowhat.rainbow.show()
time.sleep(1)

# set the third LED to yellow, and so on.
rainbowhat.rainbow.set_pixel(4, 255, 255, 0, 0.1)
rainbowhat.rainbow.show()
time.sleep(1)

# continue the pattern to add the other colours of the rainbow 
