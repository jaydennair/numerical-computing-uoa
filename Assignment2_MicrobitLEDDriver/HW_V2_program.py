'''
Hardware Lab device driver exercise 4.

Moves a pixel around the display on a micro:bit.
'''

import microbit
import machine
import HW_V2_driver as driver
import time

# micro:bit GPIO register addresses
#GPIO 0
OUT_0_address = 0x50000504
OUT_0_SET_address = 0x50000508
OUT_0_CLEAR_address = 0x5000050C
#GPIO 1
OUT_1_address = 0x50000804
OUT_1_SET_address = 0x50000808
OUT_1_CLEAR_address = 0x5000080C



# This is code to initialise the microbit registers
microbit.display.off()
machine.mem32[0x50000518]=0xFFFFFFFF
microbit.sleep(500)
machine.mem32[0x50000818]=0x000000F0
microbit.sleep(500)
machine.mem32[OUT_1_SET_address] = 0x00000020
microbit.sleep(500)



while True:
    for n in range(25):
        x = int(n/5)
        y = n % 5
        driver.display_none() 
        #testing the display_pixel function
        driver.display_pixel(x + 1, y + 1)
        microbit.sleep(500)
    