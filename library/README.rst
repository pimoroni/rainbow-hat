.. figure:: https://github.com/pimoroni/rainbow-hat/raw/master/rainbowhatpimoroni.png
   :alt: Rainbow HAT

Rainbow HAT is a flexible IO exploration board with multiple devices
covering i2c, SPI, generic GPIO.

This repository contains the Pimoroni Python driver for Rainbow HAT, for
use with Raspbiban on your Raspberry Pi.

For the official AndroidThings driver see:
https://github.com/androidthings/contrib-drivers/tree/master/rainbowhat

Installation
------------

**Full install ( recommended ):**

We've created a super-easy installation script that will install all
pre-requisites and get your Rainbow HAT up and running in a jiffy. To
run it fire up Terminal which you'll find in Menu -> Accessories ->
Terminal on your Raspberry Pi desktop like so:

.. figure:: https://github.com/pimoroni/rainbow-hat/raw/master/terminal.jpg
   :alt: Finding the terminal

In the new terminal window type:

.. code:: bash

    curl https://get.pimoroni.com/rainbowhat | bash

If you choose to download examples you'll find them in
``/home/pi/Pimoroni/rainbowhat``.

**Library install for Python 3:**

on Raspbian:

.. code:: bash

    sudo apt-get install python3-rainbowhat

other environments:

.. code:: bash

    sudo pip3 install rainbowhat

**Library install for Python 2:**

on Raspbian:

.. code:: bash

    sudo apt-get install python-rainbowhat

other environments:

.. code:: bash

    sudo pip2 install rainbowhat

Documentation & Support
-----------------------

| Getting started - http://learn.pimoroni.com/tutorial/sandyj/getting-started-with-rainbow-hat-in-python
| GPIO Pinout - https://pinout.xyz/pinout/rainbow\_hat
| Get help - http://forums.pimoroni.com/c/support
