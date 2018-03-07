# -*- coding: utf-8 -*-

import I2C_LCD_driver
import os, sys
from time import *

lcd = I2C_LCD_driver.lcd()

nbre_boot = sys.argv[1]
manques = sys.argv[2]
#print(nbre_boot, manques)
lcd.lcd_display_string("boot number:" + nbre_boot , 1)
lcd.lcd_display_string("Failed:" + manques, 2)