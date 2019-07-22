import smbus
import GE_config as cfg
import numpy as np


def init_i2c(i2cx):
    i2c = smbus.SMBus(i2cx)
    return i2c


def get_address(ad_sel):
    address = cfg.ADDRESS + int(ad_sel)
    return address


def init_grid_eye(i2cx, ad_sel):
    i2c = init_i2c(i2cx)
    address = get_address(ad_sel)
    gridEye = cfg.GridEye(i2c, address)
    return gridEye


def read_reg(gridEye, reg):
    read = gridEye.i2c.read_byte_data(gridEye.address, reg)
    return read


def write_reg(gridEye, reg, value):
    gridEye.i2c.write_byte_data(gridEye.address, reg, value)


def get_op_mode(gridEye):
    op_mode = gridEye.i2c.read_byte_data(gridEye.address, cfg.OP_MODE)
    return cfg.OpMode(op_mode).name


# when put in sleep-mode you must set normal mode to be able to read/write again from i2c
def set_op_mode(gridEye, op_mode):
    gridEye.i2c.write_byte_data(gridEye.address, cfg.OP_MODE, op_mode)


def set_frame_rate(gridEye, frame_rate):
    gridEye.i2c.write_byte_data(gridEye.address, cfg.FRAME_RATE, frame_rate)


def get_frame_rate(gridEye):
    frame_rate = gridEye.i2c.read_byte_data(gridEye.address, cfg.FRAME_RATE)
    return cfg.FrameRate(frame_rate).name


def get_pxl_matrix(gridEye):
    # can read only 32 bytes block max over i2c in 1 instruction
    pixels = np.zeros(64)
    
    for i in range (64):
        pxl = gridEye.i2c.read_i2c_block_data(gridEye.address, cfg.PXL0_VAL_LOW + i*2, 2)
        pixels[i] = ((pxl[0] + (pxl[1] << 8)) - (4096 * (pxl[1] & 0x08))) * 0.25

    return pixels
