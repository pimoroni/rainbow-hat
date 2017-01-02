.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

.. module:: rainbowhat

Welcome
-------

This documentation will guide you through the methods available in the Rainbow HAT python library.

Rainbow HAT is a Raspberry Pi add-on designed for Android Things, it includes:

* 3 capacitive touch buttons
* 3 LEDs: Red, Green and Blue
* 7 RGB LEDs (APA102)
* A four-character "star" display
* A temperature/pressure sensor


* More information - https://shop.pimoroni.com/products/rainbow-hat
* GPIO Pinout - http://pinout.xyz/pinout/rainbow_hat
* Get the code - https://github.com/pimoroni/rainbow-hat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. automethodoutline:: buzzer.note
.. automethodoutline:: buzzer.midi_note
.. automethodoutline:: buzzer.clear_timeout
.. automethodoutline:: buzzer.stop

.. automethodoutline:: rainbow.set_brightness
.. automethodoutline:: rainbow.clear
.. automethodoutline:: rainbow.show
.. automethodoutline:: rainbow.set_all
.. automethodoutline:: rainbow.set_pixel
.. automethodoutline:: rainbow.set_clear_on_exit

.. automethodoutline:: weather.temperature
.. automethodoutline:: weather.pressure
.. automethodoutline:: weather.altitude
.. automethodoutline:: weather.update

.. autoclass:: Lights
   :members:

.. autoclass:: touch
   :members:

Buzzer: Play A Note
-------------------

.. automethod:: rainbowhat.buzzer.note
   :noindex:

Buzzer: Play A Midi Note
------------------------

.. automethod:: rainbowhat.buzzer.midi_note
   :noindex:

Buzzer: Stop The Buzzer
-----------------------

.. automethod:: rainbowhat.buzzer.stop
   :noindex:

Buzzer: Clear Note-off Timeout
------------------------------

.. automethod:: rainbowhat.buzzer.clear_timeout
   :noindex:

Rainbow: Set Brightness
-----------------------

.. automethod:: rainbowhat.rainbow.set_brightness
   :noindex:

Rainbow: Clear
--------------

.. automethod:: rainbowhat.rainbow.clear
   :noindex:

Rainbow: Show
-------------

.. automethod:: rainbowhat.rainbow.show
   :noindex:

Rainbow: Set All Pixels
-----------------------

.. automethod:: rainbowhat.rainbow.set_all
   :noindex:

Rainbow: Set Single Pixel
-------------------------

.. automethod:: rainbowhat.rainbow.set_pixel
   :noindex:

Rainbow: Set Clear-on-exit
--------------------------

.. automethod:: rainbowhat.rainbow.set_clear_on_exit
   :noindex:

Weather: Get Temperature
------------------------

.. automethod:: rainbowhat.weather.temperature
   :noindex:

Weather: Get Pressure
---------------------

.. automethod:: rainbowhat.weather.pressure
   :noindex:

Weather: Get Altitutde
----------------------

.. automethod:: rainbowhat.weather.altitude
   :noindex:

Weather: Update
---------------

.. automethod:: rainbowhat.weather.update
   :noindex:

Lights
------

Rainbow HAT has three lights: Red, Green and Blue. They can be accessed by name like so:

:python:`rainbowhat.light.red`

:python:`rainbowhat.light.green`

:python:`rainbowhat.light.blue`

Each light is an instance of the :python:`Light` class, the following methods are available:

.. autoclass:: rainbowhat.lights.Light
   :noindex:
   :members:

Eg: :python:`rainbowhat.light.red.on()`

Touch
-----

Rainbow HAT has three touch inputs: A, B and C. They can be accessed lke so:

:python:`rainbowhat.touch.A`

:python:`rainbowhat.touch.B`

:python:`rainbowhat.touch.C`

Each touch input is an instance of the :python:`Button` class, the following methods are available

.. autoclass:: rainbowhat.touch.Button
   :noindex:
   :members:

You can use touch handlers either by passing in a function by name, or using the method as a decorator. Eg::

    @rainbowhat.touch.A.press():
    def press(button):
        print("A pressed!")

Or::

    def press(button):
        print("Button {} pressed!".format(button))

    rainbowhat.touch.A.press(press)
    rainbowhat.touch.B.press(press)
