# code from Learning Card 06 - Rainbow HAT

# import the rainbowhat and time modules
import rainbowhat
import time

# set all LEDs to magenta at 0.1 brightness
rainbowhat.rainbow.set_all(100, 10, 100, 0.1)

# show all the changes to the LEDs
rainbowhat.rainbow.show()

# wait 2 seconds before doing the next step
time.sleep(2)

# set just pixel 3 to green at 0.1 brightness
rainbowhat.rainbow.set_pixel(3, 0, 255, 0, 0.1)

# show all the changes to the LEDs
rainbowhat.rainbow.show()

# wait 2 seconds before doing the next step
time.sleep(2)

# set all LEDs to no colour (off) at 0 brightness
rainbowhat.rainbow.set_all(0, 0, 0, 0)

# show all the changes to the LEDs
rainbowhat.rainbow.show()
