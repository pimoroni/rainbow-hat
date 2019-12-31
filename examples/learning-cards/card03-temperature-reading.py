# code from Learning Card 02 - Rainbow HAT

# import the rainbowhat module
import rainbowhat

# create a variable to store the temperature reading in
temperature = rainbowhat.weather.temperature()

# sends the data from the reading to the display
rainbowhat.display.print_float(temperature)

# displays the data on the rainbow HAT
rainbowhat.display.show()
