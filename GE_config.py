from enum import IntEnum
from collections import namedtuple

# GridEye named tuple
GridEye = namedtuple('GridEye', ['i2c', 'address'])

# Regs
OP_MODE = 0x00	#R/W	Operating Mode
SOFT_RESET = 0x01	# W	Software Reset
FRAME_RATE = 0x02	# R/W	Frame Rate
INT_FUNC = 0x03	# R/W	Interrupt Function
INT_FLG = 0x04	# R	Interrupt Flag
INT_FLG_CLR = 0x05	# W	Interrupt Flag Clear
# = 0x06	# UNUSED
AVERAGE = 0x07	# R	Moving Average Output Mode
INT_UPP_LIM_LOW = 0x08	# R/W	Upper Interrupt Value
INT_UPP_LIM_HIGH = 0x09	# R/W	Upper Interrupt Value
INT_LOW_LIM_LOW = 0x0A	# R/W	Lower Interrupt Value
INT_LOW_LIM_HIGH = 0x0B	# R/W	Lower Interrupt Value
INT_HYST_LOW = 0x0C	# R/W	Hysteresis Interrupt Value
INT_HYST_HIGH = 0x0D	# R/W	Hysteresis Interrupt Value
THERM_VAL_LOW = 0x0E	# R	Thermistor Output Value
THERM_VAL_HIGH = 0x0F	# R	Thermistor Output Value
PXL0_7_INT_FLG = 0x10	# R	Pixel 0-7 Interrupt Flag
PXL8_15_INT_FLG = 0x11	# R	Pixel 8-15 Interrupt Flag
PXL16_23_INT_FLG = 0x12	# R	Pixel 16-23 Interrupt Flag
PXL24_31_INT_FLG = 0x13	# R	Pixel 24-31 Interrupt Flag
PXL32_39_INT_FLG = 0x14	# R	Pixel 32-39 Interrupt Flag
PXL40_47_INT_FLG = 0x15	# R	Pixel 40-47 Interrupt Flag
PXL48_55_INT_FLG = 0x16	# R	Pixel 48-55 Interrupt Flag
PXL56_63_INT_FLG = 0x17	# R	Pixel 56-63 Interrupt Flag
#0x18	# -	- unused
#...	-	# -
#0x7F	# -	-
PXL0_VAL_LOW = 0x80	# R	Pixel 0 Output Value (low)
PXL0_VAL_HIGH = 0x81	# R	Pixel 0 Output Value (high)
# ... USE PXL0_VAL_X + PXL_ID TO GET THE RIGHT REG #
PXL64_VAL_LOW = 0xFE	# R	Pixel 63 Output Value (low)
PXL64_VAL_HIGH = 0xFF	# R	Pixel 63 Output Value (high)

# OpMode Enum
class OpMode(IntEnum):
    NORMAL_MODE = 0x00
    SLEEP_MODE = 0x10
    STAND_BY_60_SEC = 0x20
    STAND_BY_10_SEC = 0x21

# FrameRate Enum
class FrameRate(IntEnum):
    FR_1FPS = 0x01
    FPS_10FPS = 0x00    

# I2C0 for older RPi, I2C1 for RPi 3+
I2C0 = 0
I2C1 = 1

# I2C slave address
# AD_SEL_GND if pin AD_SELECT is connected to GND
# AD_SEL_VDD if pin AD_SELECT is connected to VDD
ADDRESS = 0x68
AD_SEL_GND = False
AD_SEL_VDD = True