import RPi.GPIO as GPIO


RED = 6
GREEN = 19
BLUE = 26

GPIO.setmode(GPIO.BCM)

class Light:
    def __init__(self, gpio_pin):
        self._gpio_pin = gpio_pin
        self.state = False
        GPIO.setup(self._gpio_pin, GPIO.OUT, initial=GPIO.LOW)

    def on(self):
        self.write(True)

    def off(self):
        self.write(False)

    def toggle(self):
        self.write(not self.state)

    def write(self, value):
        self.state = GPIO.HIGH if value else GPIO.LOW
        GPIO.output(self._gpio_pin, self.state)

class Lights:
    red = Light(RED)
    green = Light(GREEN)
    blue = Light(BLUE)

    _all = [red, green, blue]

    def __getitem__(self, key):
        return self._all[key] 

    def all(self, value):
        self.red.write(value > 0)
        self.green.write(value > 0)
        self.blue.write(value > 0)

    def rgb(self, r, g, b):
        """Set the LEDs by colour."""
        self.red.write(r > 0)
        self.green.write(g > 0)
        self.blue.write(b > 0)

Lights = Lights()
