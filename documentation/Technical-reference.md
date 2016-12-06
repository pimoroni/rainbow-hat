#Technical Reference

## Temperature/Pressure via BMP280, i2c: 0x77

Temperature and Pressure readings are supplied by the BMP280.

See the BMP280 datasheet for details.

## 4-digit Alphanumeric Character Display via HT16K33, i2c: 0x70

The HT16K33 controller is connected to four, 14-segment star displays with decimal points.

See the HT16K33 datasheet for details.

## Piezo Transducer

The piezo transducer is connected to BCM#13 / PWM1.

## 7 Element APA102 Rainbow via SPI0 with chip-select CE0

The rainbow arc consists of 7 APA102 RGB pixels numbered 0 to 6 from right to left.

Function | GPIO Pin
---------|---------
Clock    | BCM#11
Data     | BCM#19
Chip-Sel | BCM#8

It's a write-only device requiring a 37 byte update transaction.

* Start frame of 32 zero bits
* Data for seven 32 bit pixels:
 * 8-bit start frame of 0b11100000 + 5bit brightness value
 * 8-bit blue value
 * 8-bit green value
 * 8-bit red value
* End frame of at least 36 zero bits

## 3 Touch Inputs via AT42QT1070

The 3 touch inputs, labelled A, B and C, are driven by an AT42QT1070 QTouch controller.

The pins are active low, and should be set up as inputs with the pull-up resistors enabled.

Input | GPIO Pin
------|---------
A     | BCM#21
B     | BCM#20
C     | BCM#16

## 3 LEDs, Red, Green and Blue via GPIO

The 3 LEDs are connected to the following GPIO pins.

Each is connected via a 1k current limiting resistor.

LED   | GPIO Pin
------|---------
Red   | BCM#6
Green | BCM#19
Blue  | BCM#26

