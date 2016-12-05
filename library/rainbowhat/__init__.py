from .i2c_bus import bus
from . import apa102
from .bmp280 import bmp280
from .alphanum4 import AlphaNum4
from . import touch
from . import lights

display = AlphaNum4(i2c=bus)
display.begin()

weather = bmp280(bus)
rainbow = apa102
buzzer = None
