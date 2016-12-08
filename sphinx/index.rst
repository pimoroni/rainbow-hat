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
