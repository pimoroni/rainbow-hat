# code from Learning Card 04 - Rainbow HAT

# import the rainbowhat module
import rainbowhat

# create a variable to store the pressure reading in
pres = rainbowhat.weather.pressure()

# sends the data from the reading to the display
rainbowhat.display.print_float(pres)

# displays the data on the rainbow HAT
rainbowhat.display.show()
