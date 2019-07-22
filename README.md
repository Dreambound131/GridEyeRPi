# GridEyeRPi
Library to communicate with GridEye sensor via I2C on the Raspberry Pi w/ python3 

In GE_config.py are all the constant and Enum used in GridEye.py

# Example
first import GridEye and GE_config and numpy

```
import GridEye as ge
import GE_config as cfg
import numpy as np
```

then you call init_grid_eye func to init the I2C bus

```
gridEye = GridEye.init_grid_eye(cfg.I2C1, cfg.AD_SEL_GND)
```

At this point you can just call get_pxl_matrix to get the 64 pixel np.array already converted in °C
```
res = GridEye.get_pxl_matrix(gridEye)
```
