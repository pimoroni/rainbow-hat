
__version__ = '0.0.2'


is_setup = False


class Default(object):
    """Default class to catch calls and ensure one-time setup.
    """

    def __init__(self, parent_name=None, **kwargs):
        object.__init__(self)
        self._parent_name = parent_name

    def _ensure_setup(self):
        setup()
        self._ensure_setup = lambda: globals()[self._parent_name]
        return globals()[self._parent_name]

    def __getattribute__(self, name):
        if name in ["_ensure_setup", "_parent_name"]:
             return object.__getattribute__(self, name)

        return self._ensure_setup().__getattribute__(name)

    def __repr__(self):
        return self._ensure_setup().__repr__()

    def __getitem__(self, item):
        return self._ensure_setup()[item]


def setup():
    global is_setup, display, touch, lights, weather, rainbow

    if is_setup:
        return

    from .i2c_bus import bus
    from . import apa102
    from .bmp280 import bmp280
    from .alphanum4 import AlphaNum4
    from .touch import Buttons
    from .lights import Lights
    from . import buzzer

    display = AlphaNum4(i2c=bus)

    try:
        display.begin()
    except IOError as e:
        raise IOError(e.errno, "HT16K33 display not responding. Is Rainbow HAT connected?")

    display.clear()
    display.show()

    touch = Buttons
    lights = Lights
    weather = bmp280(bus)
    rainbow = apa102

    is_setup = True

display = Default('display')
touch = Default('touch')
lights = Default('lights')
weather = Default('weather')
rainbow = Default('rainbow')

