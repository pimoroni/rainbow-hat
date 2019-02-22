#coding: utf-8

import time


ADDR = 0x77

# this value is necessary to calculate the correct height above sealevel
# its also included in airport weather information ATIS named as QNH
# unit is hPa
QNH = 1020

# power mode
# POWER_MODE = 0 # sleep mode
# POWER_MODE = 1 # forced mode
# POWER_MODE = 2 # forced mode
POWER_MODE = 3   # normal mode

# temperature resolution
# OSRS_T = 0 # skipped
# OSRS_T = 1 # 16 Bit
# OSRS_T = 2 # 17 Bit
# OSRS_T = 3 # 18 Bit
# OSRS_T = 4 # 19 Bit
OSRS_T = 5   # 20 Bit

# pressure resolution
# OSRS_P = 0 # pressure measurement skipped
# OSRS_P = 1 # 16 Bit ultra low power
# OSRS_P = 2 # 17 Bit low power
# OSRS_P = 3 # 18 Bit standard resolution
# OSRS_P = 4 # 19 Bit high resolution
OSRS_P = 5   # 20 Bit ultra high resolution

# filter settings
# FILTER = 0 #
# FILTER = 1 #
# FILTER = 2 #
# FILTER = 3 #
FILTER = 4
# FILTER = 5 #
# FILTER = 6 #
# FILTER = 7 #

# standby settings
# T_SB = 0 # 000 0,5ms
# T_SB = 1 # 001 62.5 ms
# T_SB = 2 # 010 125 ms
# T_SB = 3 # 011 250ms
T_SB = 4   # 100 500ms
# T_SB = 5 # 101 1000ms
# T_SB = 6 # 110 2000ms
# T_SB = 7 # 111 4000ms


CONFIG = (T_SB << 5) + (FILTER << 2)                    # combine bits for config
CTRL_MEAS = (OSRS_T << 5) + (OSRS_P << 2) + POWER_MODE  # combine bits for ctrl_meas

# print ("CONFIG:",CONFIG)
# print ("CTRL_MEAS:",CTRL_MEAS)

REGISTER_DIG_T1 = 0x88
REGISTER_DIG_T2 = 0x8A
REGISTER_DIG_T3 = 0x8C
REGISTER_DIG_P1 = 0x8E
REGISTER_DIG_P2 = 0x90
REGISTER_DIG_P3 = 0x92
REGISTER_DIG_P4 = 0x94
REGISTER_DIG_P5 = 0x96
REGISTER_DIG_P6 = 0x98
REGISTER_DIG_P7 = 0x9A
REGISTER_DIG_P8 = 0x9C
REGISTER_DIG_P9 = 0x9E
REGISTER_CHIPID = 0xD0
REGISTER_VERSION = 0xD1
REGISTER_SOFTRESET = 0xE0
REGISTER_CONTROL = 0xF4
REGISTER_CONFIG = 0xF5
REGISTER_STATUS = 0xF3
REGISTER_TEMPDATA_MSB = 0xFA
REGISTER_TEMPDATA_LSB = 0xFB
REGISTER_TEMPDATA_XLSB = 0xFC
REGISTER_PRESSDATA_MSB = 0xF7
REGISTER_PRESSDATA_LSB = 0xF8
REGISTER_PRESSDATA_XLSB = 0xF9


class signed_int(int):
    """Convert int to signed."""

    def __new__(self, number, bits=16):
        if number & (1 << (bits - 1)):
            number -= 1 << bits
        return int.__new__(self, number)


class bmp280(object):
    """BMP280 Temperature Sensor."""

    def __init__(self, i2c_bus=None, addr=ADDR):
        """Initialise BMP280."""
        object.__init__(self)

        self._temperature = 0
        self._pressure = 0

        self.addr = addr
        self.i2c_bus = i2c_bus
        self._is_setup = False

        if getattr(i2c_bus, "write_byte_data", None) is None or getattr(i2c_bus, "read_byte_data", None) is None:
            raise TypeError("Object given for i2c_bus must implement write_byte_data and read_byte_data methods")

    def _write_byte(self, register, value):
        self.i2c_bus.write_byte_data(self.addr, register, value)

    def _read_byte(self, register):
        return self.i2c_bus.read_byte_data(self.addr, register)

    def _read_word(self, register):
        return self.i2c_bus.read_word_data(self.addr, register)

    def _read_signed_word(self, register):
        word = self._read_word(register)
        return signed_int(word)

    def _read_unsigned_word(self, register):
        return self._read_word(register)

    def temperature(self):
        """Return the current temperature.

        Note: This value may be affected by nearby sources of heat, including the Pi itself.

        """
        self.update()
        return self._temperature

    def pressure(self):
        """Return the current air pressure."""
        self.update()
        return self._pressure

    def altitude(self, qnh=QNH):
        """Return the current approximate altitude.

        :param qnh: Your local value for atmospheric pressure adjusted to sea level.

        """
        # Calculate altitute from pressure & qnh
        return 44330.0 * (1.0 - pow(self.pressure() / (qnh * 100), (1.0 / 5.255)))

    def update(self):
        """Update stored temperature and pressure values.

        This function is called automatically when calling temperature() or pressure().

        """
        if not self._is_setup:
            if self._read_byte(REGISTER_CHIPID) == 0x58:    # check sensor id 0x58=BMP280
                self._write_byte(REGISTER_SOFTRESET, 0xB6)  # reset sensor
                time.sleep(0.2)
                self._write_byte(REGISTER_CONTROL, CTRL_MEAS)
                time.sleep(0.2)
                self._write_byte(REGISTER_CONFIG, CONFIG)
                time.sleep(0.2)

                # read compensation settings
                self.dig_T1 = self._read_unsigned_word(REGISTER_DIG_T1)
                self.dig_T2 = self._read_signed_word(REGISTER_DIG_T2)
                self.dig_T3 = self._read_signed_word(REGISTER_DIG_T3)
                self.dig_P1 = self._read_unsigned_word(REGISTER_DIG_P1)
                self.dig_P2 = self._read_signed_word(REGISTER_DIG_P2)
                self.dig_P3 = self._read_signed_word(REGISTER_DIG_P3)
                self.dig_P4 = self._read_signed_word(REGISTER_DIG_P4)
                self.dig_P5 = self._read_signed_word(REGISTER_DIG_P5)
                self.dig_P6 = self._read_signed_word(REGISTER_DIG_P6)
                self.dig_P7 = self._read_signed_word(REGISTER_DIG_P7)
                self.dig_P8 = self._read_signed_word(REGISTER_DIG_P8)
                self.dig_P9 = self._read_signed_word(REGISTER_DIG_P9)

            else:
                raise IOError("bmp280 not found on address {:x}".format(self.addr))

            self._is_setup = True

        raw_temp_msb = self._read_byte(REGISTER_TEMPDATA_MSB)
        raw_temp_lsb = self._read_byte(REGISTER_TEMPDATA_LSB)
        raw_temp_xlsb = self._read_byte(REGISTER_TEMPDATA_XLSB)
        raw_press_msb = self._read_byte(REGISTER_PRESSDATA_MSB)
        raw_press_lsb = self._read_byte(REGISTER_PRESSDATA_LSB)
        raw_press_xlsb = self._read_byte(REGISTER_PRESSDATA_XLSB)

        # combine 3 bytes  msb 12 bits left, lsb 4 bits left, xlsb 4 bits right
        raw_temp = (raw_temp_msb << 12) + (raw_temp_lsb << 4) + (raw_temp_xlsb >> 4)

        # combine 3 bytes  msb 12 bits left, lsb 4 bits left, xlsb 4 bits right
        raw_press = (raw_press_msb << 12) + (raw_press_lsb << 4) + (raw_press_xlsb >> 4)

        var1 = (raw_temp / 16384.0 - self.dig_T1 / 1024.0) * self.dig_T2
        var2 = (raw_temp / 131072.0 - self.dig_T1 / 8192.0) * (raw_temp / 131072.0 - self.dig_T1 / 8192.0) * self.dig_T3
        temp = (var1 + var2) / 5120.0

        # store fine temperature for pressure calculation
        t_fine = (var1 + var2)

        var1 = t_fine / 2.0 - 64000.0
        var2 = var1 * var1 * self.dig_P6 / 32768.0
        var2 = var2 + var1 * self.dig_P5 * 2
        var2 = var2 / 4.0 + self.dig_P4 * 65536.0
        var1 = (self.dig_P3 * var1 * var1 / 524288.0 + self.dig_P2 * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self.dig_P1
        press = 1048576.0 - raw_press
        press = (press - var2 / 4096.0) * 6250.0 / var1
        var1 = self.dig_P9 * press * press / 2147483648.0
        var2 = press * self.dig_P8 / 32768.0
        press = press + (var1 + var2 + self.dig_P7) / 16.0
        press /= 100  # convert to hPa

        self._temperature = temp
        self._pressure = press
