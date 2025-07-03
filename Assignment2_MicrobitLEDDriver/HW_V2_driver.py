'''
Assignment 2 micro:bit V2 LED device driver.

#This program implements an LED device driver utilising the multiplexing logic
#in order to manipulate the state of various pixels in the 5x5 LED grid
#various functions are implemented in the program in order to aid in the pixel manipulation
#including such as illuminating one pixel at a time, 
#displaying on/off all pixels, and illuminating diagonal pixels
'''
import machine, microbit, time

# micro:bit GPIO register addresses
#GPIO 0
OUT_0_address = 0x50000504
OUT_0_SET_address = 0x50000508
OUT_0_CLEAR_address = 0x5000050C
#GPIO 1
OUT_1_address = 0x50000804
OUT_1_SET_address = 0x50000808
OUT_1_CLEAR_address = 0x5000080C

#row pin bitmasks - GPIO 0 
row_pin    = [0, 0x00200000, 0x00400000, 0x00008000, 0x01000000, 0x00080000]


#column pin bitmasks - GPIO 0 (except row 4 - GPIO 1)
column_pin = [0, 0x10000000, 0x00000800, 0x80000000, 0x00000020, 0x40000000]

def display_none():
    '''
    Turn off all pixels.
    TODO: Complete the function using only machine.mem32[OUT_n_CLEAR_address] and machine.mem32[OUT_n_SET_address] assignments.
    '''
    # A pixel will be off if the row pin is 0 or the column pin is 1.
    # Column 4 will be 1 by setting GPIO 1 pin 5 to 1
    #Turn off column 4 on GPIO 1
    machine.mem32[OUT_1_SET_address] = column_pin[4]
    #set rows to LOW (turn off all rows)
    machine.mem32[OUT_0_CLEAR_address] = (
        row_pin[1] | row_pin[2] | row_pin[3] | row_pin[4] | row_pin[5]
    )
    #set columns to HIGH (turn off all columns)
    machine.mem32[OUT_0_SET_address] = (
      column_pin[1] | column_pin[2] | column_pin[3] | column_pin[5])

    
    

def display_all():
    '''
    '''
    #ground column 4 by clearing the bit (switch it ON)
    machine.mem32[OUT_1_CLEAR_address] = column_pin[4]

    #set rows to LOW (turn off all rows)
    machine.mem32[OUT_0_SET_address] = (
        row_pin[1] | row_pin[2] | row_pin[3] | row_pin[4] | row_pin[5]
    )
    #set columns to HIGH (turn off all columns)
    machine.mem32[OUT_0_CLEAR_address] = (
      column_pin[1] | column_pin[2] | column_pin[3] | column_pin[5])

    
def display_pixel(r, c):
    '''
    '''
    # A pixel will be on if the row pin is 1 and the column pin is 0.
    # Row row will be 1 by setting GPIO 0 pin row_pin[row] to 1
    machine.mem32[OUT_0_SET_address] = row_pin[r]
    if c == 4:
        #Column four is located on GPIO 1
        machine.mem32[OUT_1_CLEAR_address] = column_pin[c]
    else:
        #All other columns are located on GPIO 0
        machine.mem32[OUT_0_CLEAR_address] = column_pin[c]

def display_pixel_list(rc_list, ms = 1000):
    '''
    '''
    start = time.ticks_ms()
    #keeps looping until the time elapsed since start is less than ms
    while time.ticks_diff(time.ticks_ms(), start) < ms:

        #cyle through each row and col of rc_list
        #and display the pixel
        for r, c in rc_list:
            display_none()
            display_pixel(r,c)
            microbit.sleep(5)
            #leave the pixel on for 5 milliseconds
            
        




    
    
def main():
    '''
    Standalone test of device driver.
    '''

    # This is code to initialise the microbit registers
    microbit.display.off()
    machine.mem32[0x50000518]=0xFFFFFFFF
    microbit.sleep(500)
    machine.mem32[0x50000818]=0x000000F0
    microbit.sleep(500)
    machine.mem32[OUT_1_SET_address] = 0x00000020
    microbit.sleep(500)

    #Task 2 - producing a 3x3 LED grid

    #allow for custom control over LED display
    microbit.display.off()

    #turn off all rows and columns - except for column 4
    machine.mem32[OUT_0_address] = 0x01688000

    #turn off row 2
    machine.mem32[OUT_0_CLEAR_address] = 0x00400000

    #turn off columns: 1 and 2
    machine.mem32[OUT_0_SET_address] = 0x10000800

    #turn on rows: 1, 3 and 5
    machine.mem32[OUT_0_SET_address] = 0x00288000

    #turn off row 4 while turning on columns 1, 3 and 5
    machine.mem32[OUT_0_CLEAR_address] = 0xD1000000

    #display the 3x3 LED grid pattern for 3 seconds
    microbit.sleep(3000)

    #tests functionality of display_all() and display_none()
    #This for loop causes all the pixels in the 
    #microbit to flash 5 times, with a 0.5 second delay
    #in between each flash
    for _ in range(5):
        display_all()
        microbit.sleep(500)
        display_none()
        microbit.sleep(500)


    #tests functionality of pixel_display
    #This nested for loop loops around each r,c
    #causing it to flash it's corresponding pixel one at a time until
    #every pixel in the 5x5 grid was activated
    for r in range(1,6):
        for c in range(1,6):
            display_pixel(r,c)
            microbit.sleep(500)
            display_none()
            #turn of all pixels
            
    #tests functionality of display_pixel_list
    #turns on main diagonal pixels
    main_diagonal = [(i, i) for i in range(1,6)]
    display_pixel_list(main_diagonal, 500)

    #turns on secondary diagonal pixels  
    secondary_diagonal = [(i, 6 - i) for i in range(1,6)]
    display_pixel_list(secondary_diagonal, 500)

    #turns on all pixels
    display_all()
    

if __name__ == "__main__":
    main()