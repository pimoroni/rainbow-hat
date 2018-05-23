
__version__ = '0.1.0'

from . import apa102
from .bmp280 import bmp280
from .alphanum4 import AlphaNum4
from .touch import Buttons
from .lights import Lights
from . import buzzer
from sys import version_info

try:
    import smbus
except ImportError:
    if version_info[0] < 3:
        raise ImportError("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        raise ImportError("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

try:
    import RPi.GPIO as GPIO
except ImportError:
    if version_info[0] < 3:
        raise ImportError("This library requires python-rpi.gpio\nInstall with: sudo apt-get install python-rpi.gpio")
    elif version_info[0] == 3:
        raise ImportError("This library requires python3-rpi.gpio\nInstall with: sudo apt-get install python3-rpi.gpio")

bus = None

if GPIO.RPI_REVISION == 2 or GPIO.RPI_REVISION == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

display = AlphaNum4(i2c=bus)
touch = Buttons
lights = Lights
weather = bmp280(bus)
rainbow = apa102

