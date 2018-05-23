from threading import Timer

try:
    import RPi.GPIO as GPIO
except ImportError:
    raise ImportError("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")


BUZZER = 13

_timeout = None

_is_setup = False

pwm = None

def setup():
    global _is_setup, pwm

    if _is_setup:
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZER, GPIO.OUT)

    # Set up the PWM and then set the pin to input
    # to prevent the signal from being output.
    # Since starting/stopping PWM causes a segfault,
    # this is the only way to manage the buzzer.

    pwm = GPIO.PWM(BUZZER, 1)
    GPIO.setup(BUZZER, GPIO.IN)
    pwm.start(50)

    _is_setup = True

def note(frequency, duration=1.0):
    """Play a single note.

    :param frequency: Musical frequency in hertz
    :param duration: Optional duration in seconds, use None to sustain note

    """

    global _timeout

    setup()

    if frequency <= 0:
        raise ValueError("Frequency must be > 0")

    if duration is not None and duration <= 0:
        raise ValueError("Duration must be > 0")

    clear_timeout()

    pwm.ChangeFrequency(frequency)
    GPIO.setup(BUZZER, GPIO.OUT)    

    if duration is not None and duration > 0:
        _timeout = Timer(duration, stop)
        _timeout.start()

def midi_note(note_number, duration=1.0):
    """Play a single note by MIDI note number.

    Converts a MIDI note number into a frequency and plays it. A5 is 69.

    :param note_number: MIDI note number of note
    :param duration: Optional duration in seconds, use None to sustain note

    """

    freq = (2**((note_number-69.0)/12)) * 440

    note(freq, duration)

def clear_timeout():
    """Clear any note timeout set.

    Will cause any pending playing note to be sustained.

    """

    global _timeout

    if _timeout is not None:
        _timeout.cancel()
        _timeout = None

def stop():
    """Stop buzzer.

    Immediately silences the buzzer.

    """

    clear_timeout()

    GPIO.setup(BUZZER, GPIO.IN)

