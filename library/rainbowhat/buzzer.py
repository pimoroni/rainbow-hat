import RPi.GPIO as GPIO
import time
import threading
import atexit


BUZZER = 13


_running = True
_t = None
_note_queue = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

pwm = GPIO.PWM(BUZZER, 1)
GPIO.setup(BUZZER, GPIO.IN)
pwm.start(50)

def note(frequency, duration, duty=0.5):
    if duration <= 0:
        raise ValueError("Duration must be > 0")
    if frequency <= 0 and frequency is not None:
        raise ValueError("Frequency must be > 0")

    _note_queue.append((frequency, duration, duty))

def _run():
    global _running, _note_queue

    _running = True

    while _running:
        try:
            frequency, duration, duty = _note_queue.pop(0)
            if frequency is None:
                time.sleep(duration)
                continue

            pwm.ChangeFrequency(frequency)
            GPIO.setup(BUZZER, GPIO.OUT)
            time.sleep(duration * duty)
            GPIO.setup(BUZZER, GPIO.IN)
            time.sleep(duration - (duration * duty))
        except IndexError:
            time.sleep(0.001)

def _stop():
    global _running, _t

    _running = False
    if _t is not None:
        _t.join()

atexit.register(_stop)
_t = threading.Thread(target=_run)
_t.daemon = True
_t.start()

