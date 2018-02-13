try:
    import RPi.GPIO as GPIO
except ImportError:
    raise ImportError("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


PIN_A = 21
PIN_B = 20
PIN_C = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Button(object):
    def __init__(self, index, gpio_pin):
        object.__init__(self)
        self.pressed = False
        self._on_press_handler = None
        self._on_release_handler = None
        self._gpio_pin = gpio_pin
        self._index = index
        self._is_setup = False

    def setup(self):
        if self._is_setup:
            return

        GPIO.setup(self._gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._gpio_pin, GPIO.BOTH, bouncetime=1, callback=self._handle_button)
        self._is_setup = True

    def _handle_button(self, pin):
        self.pressed = GPIO.input(pin) != GPIO.HIGH

        if self.pressed and callable(self._on_press_handler):
            try:
                self._on_press_handler(self._index, self._gpio_pin)
            except TypeError:
                self._on_press_handler(self._index)

        elif callable(self._on_release_handler):
            try:
                self._on_release_handler(self._index, self._gpio_pin)
            except TypeError:
                self._on_release_handler(self._index)

    def press(self, handler=None):
        """Bind a function to handle touch press."""

        self.setup()

        if handler is None:
            def decorate(handler):
                self._on_press_handler = handler

            return decorate

        self._on_press_handler = handler

    def release(self, handler=None):
        """Bind a funciton to handle touch release."""

        self.setup()

        if handler is None:
            def decorate(handler):
                self._on_release_handler = handler

            return decorate

        self._on_release_handler = handler

class Buttons(object):
    A = Button(0, PIN_A)
    B = Button(1, PIN_B)
    C = Button(2, PIN_C)

    _all = [A, B, C]

    def __getitem__(self, key):
        return self._all[key]

    def press(self, handler=None):
        if handler is None:
            def decorate(handler):
                self.A.press(handler)
                self.B.press(handler)
                self.C.press(handler)

            return decorate

        self.A.press(handler)
        self.B.press(handler)
        self.C.press(handler)

    def release(self, handler=None):
        if handler is None:
            def decorate(handler):
                self.A.release(handler)
                self.B.release(handler)
                self.C.release(handler)

            return decorate

        self.A.release(handler)
        self.B.release(handler)
        self.C.release(handler)


Buttons = Buttons()

