import RPi.GPIO as GPIO


RED = 6
GREEN = 19
BLUE = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup([RED,GREEN,BLUE], GPIO.OUT, initial=GPIO.LOW)

def set(index, value):
    try:
        GPIO.output([RED,GREEN,BLUE][index], value)
    except IndexError:
        raise ValueError("index should be between 0 and 2")

def red(value):
    GPIO.output(RED, value)

def green(value):
    GPIO.output(GREEN, value)

def blue(value):
    GPIO.output(BLUE, value)

def all(value):
    red(value)
    green(value)
    blue(value)

def rgb(r, g, b):
    red(r > 0)
    green(g > 0)
    blue(b > 0)

def on(led):
    GPIO.output(led, GPIO.HIGH)

def off(led):
    GPIO.output(led, GPIO.LOW)
