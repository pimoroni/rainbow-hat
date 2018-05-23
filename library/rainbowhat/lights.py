try:
    import RPi.GPIO as GPIO
except ImportError:
    raise ImportError("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


RED = 6
GREEN = 19
BLUE = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Light(object):
    def __init__(self, gpio_pin):
        object.__init__(object)
        self._is_setup = False
        self._gpio_pin = gpio_pin
        self.state = False

    def on(self):
        """Turn the light on."""

        self.write(True)

    def off(self):
        """Turn the light off."""

        self.write(False)

    def toggle(self):
        """Toggle the light."""

        self.write(not self.state)

    def write(self, value):
        """Write a value to the light.

        :param value: Either True or False to turn light on or off/

        """

        if not self._is_setup:
            GPIO.setup(self._gpio_pin, GPIO.OUT, initial=GPIO.LOW)
            self._is_setup = True

        self.state = GPIO.HIGH if value else GPIO.LOW
        GPIO.output(self._gpio_pin, self.state)

class Lights(object):
    red = Light(RED)
    green = Light(GREEN)
    blue = Light(BLUE)

    _all = [red, green, blue]

    def __getitem__(self, key):
        return self._all[key] 

    def all(self, value):
        """Set a value to all lights.

        :param value: Either True or False for on/off.

        """

        self.red.write(value > 0)
        self.green.write(value > 0)
        self.blue.write(value > 0)

    def rgb(self, r, g, b):
        """Set the LEDs by colour.

        :param r: Either True or False to turn Red light on/off.
        :param g: Either True or False to turn Green light on/off.
        :param b: EIther True or False to turn Blue light on/off.

        """

        self.red.write(r > 0)
        self.green.write(g > 0)
        self.blue.write(b > 0)

Lights = Lights()
