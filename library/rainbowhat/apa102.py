import atexit
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    raise ImportError("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


DAT = 10
CLK = 11
CS = 8
NUM_PIXELS = 7
BRIGHTNESS = 7

pixels = [[0,0,0,BRIGHTNESS]] * NUM_PIXELS

_gpio_setup = False
_clear_on_exit = True

def _exit():
    if _clear_on_exit:
        clear()
        show()
    GPIO.cleanup()

def set_brightness(brightness):
    """Set the brightness of all pixels

    :param brightness: Brightness: 0.0 to 1.0
    """

    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")

    for x in range(NUM_PIXELS):
        pixels[x][3] = int(31.0 * brightness) & 0b11111

def clear():
    """Clear the pixel buffer"""
    for x in range(NUM_PIXELS):
        pixels[x][0:3] = [0,0,0]

def _write_byte(byte):
    for x in range(8):
        GPIO.output(DAT, byte & 0b10000000)
        GPIO.output(CLK, 1)
        time.sleep(0.0000005)
        byte <<= 1
        GPIO.output(CLK, 0)
        time.sleep(0.0000005)

# Emit exactly enough clock pulses to latch the small dark die APA102s which are weird
# for some reason it takes 36 clocks, the other IC takes just 4 (number of pixels/2)
def _eof():
    GPIO.output(DAT, 0)
    for x in range(36):
        GPIO.output(CLK, 1)
        time.sleep(0.0000005)
        GPIO.output(CLK, 0)
        time.sleep(0.0000005)


def _sof():
    GPIO.output(DAT,0)
    for x in range(32):
        GPIO.output(CLK, 1)
        time.sleep(0.0000005)
        GPIO.output(CLK, 0)
        time.sleep(0.0000005)


def show():
    """Output the buffer"""
    global _gpio_setup

    if not _gpio_setup:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup([DAT,CLK,CS],GPIO.OUT)
        _gpio_setup = True

    GPIO.output(CS, 0)
    _sof()

    for pixel in pixels:
        r, g, b, brightness = pixel
        _write_byte(0b11100000 | brightness)
        _write_byte(b)
        _write_byte(g)
        _write_byte(r)

    _eof()
    GPIO.output(CS, 1)

def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels

    If you don't supply a brightness value, the last value set for each pixel be kept.

    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for x in range(NUM_PIXELS):
        set_pixel(x, r, g, b, brightness)

def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel
    
    If you don't supply a brightness value, the last value will be kept.

    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    if x >= NUM_PIXELS:
        raise ValueError("Invalid pixel index {}, should be (0-{})".format(x, NUM_PIXELS-1))

    if brightness is None:
        brightness = pixels[x][3]
    else:
        brightness = int(31.0 * brightness) & 0b11111

    pixels[x] = [int(r) & 0xff,int(g) & 0xff,int(b) & 0xff,brightness]

def set_clear_on_exit(value=True):
    """Set whether the APA102 should be cleared upon exit

    By default the APA102 will turn off the pixels on exit, but calling::

        set_clear_on_exit(False)

    Will ensure that it does not.

    :param value: True or False (default True)
    """
    global _clear_on_exit
    _clear_on_exit = value

atexit.register(_exit)

