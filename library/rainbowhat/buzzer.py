from threading import Timer

import RPi.GPIO as GPIO

BUZZER = 13

_timeout = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

pwm = GPIO.PWM(BUZZER, 1)
GPIO.setup(BUZZER, GPIO.IN)
pwm.start(50)

def note(frequency, duration=1.0):
    global _timeout

    if frequency <= 0:
        raise ValueError("Frequency must be > 0")

    clear_timeout()

    pwm.ChangeFrequency(frequency)
    GPIO.setup(BUZZER, GPIO.OUT)
    
    _timeout = Timer(duration, stop)
    _timeout.start()

def clear_timeout():
    global _timeout

    if _timeout is not None:
        _timeout.cancel()
        _timeout = None

def stop():
    clear_timeout()

    GPIO.setup(BUZZER, GPIO.IN)

