import RPi.GPIO as GPIO


RED = 6
GREEN = 19
BLUE = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup([RED,GREEN,BLUE], GPIO.OUT, initial=GPIO.LOW)

def set(index, value):
    """Set a particular LED to on/off.

    :param index: Position of led from left to right: 0, 1 or 2
    :param value: Either 1 or 0 for on or off

    """

    try:
        GPIO.output([RED,GREEN,BLUE][index], value)
    except IndexError:
        raise ValueError("index should be between 0 and 2")

def red(value):
    """Set the red LED on or off."""
    GPIO.output(RED, value)

def green(value):
    """Set the green LED on or off."""
    GPIO.output(GREEN, value)

def blue(value):
   """Set the blue LED on or off."""
    GPIO.output(BLUE, value)

def all(value):
    """Set all LEDs on or off."""
    red(value)
    green(value)
    blue(value)

def rgb(r, g, b):
    """Set the LEDs by colour."""
    red(r > 0)
    green(g > 0)
    blue(b > 0)

def on(led):
    """Set a particular LED on."""
    GPIO.output(led, GPIO.HIGH)

def off(led):
    """Set a particular LED off."""
    GPIO.output(led, GPIO.LOW)

