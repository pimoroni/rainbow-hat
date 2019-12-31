# code from Project 01 - Rainbow HAT

# import the rainbowhat and time modules
import rainbowhat
import time

# a while True loop keeps doing things until interrupted
while True:

    # take the temperature and show it on the display
    temperature = rainbowhat.weather.temperature()
    rainbowhat.display.print_float(temperature)
    rainbowhat.display.show()

    # if the temperature is less than 25, just use blue
    if temperature < 25:
        blue = 255 - (temperature * 6)
        rainbowhat.rainbow.set_all(0, 0, blue, brightness=0.1)
        rainbowhat.rainbow.show()

    # if the temperature is more than 25, use green and red
    # combined to make shades of red and orange
    else:
        green = 255 - (temperature * 6)
        rainbowhat.rainbow.set_all(255, green, 0, brightness=0.1)
        rainbowhat.rainbow.show()

    # wait 10 seconds before taking the temperature again
    time.sleep(10)
