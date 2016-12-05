import RPi.GPIO as GPIO


A = 21
B = 20
C = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup([A, B, C], GPIO.IN, pull_up_down=GPIO.PUD_UP)

_buttons = {}
_button_press = {}
_button_release = {}

def _handle_button(pin):
    _buttons[pin] = GPIO.input(pin) != GPIO.HIGH

    try:
        if _buttons[pin]: # Touch
            _button_press[pin](pin)
        else: # Release
            _button_release[pin](pin)

    except KeyError:
        pass

def _assign_handler(target, button, handler):
    if button is None:
        target[A] = handler
        target[B] = handler
        target[C] = handler

    target[button] = handler

def on_touch(button=None, handler=None):
    global _button_press

    if handler is None:
        def decorate(handler):
            global _button_press
            _assign_handler(_button_press, button, handler)

        return decorate

    _assign_handler(_button_press, button, handler)

def on_release(button=None, handler=None):
    global _button_release

    if handler is None:
        def decorate(handler):
            global _button_release
            _assign_handler(_button_release, button, handler)

        return decorate

    _assign_handler(_button_release, button, handler)

for btn in [A, B, C]:
    GPIO.add_event_detect(btn, GPIO.BOTH, callback=_handle_button)
