import machine
import utime

import array, time
from machine import Pin
import rp2
from rp2 import PIO, StateMachine, asm_pio
# LED引脚
led_onboard = machine.Pin(25, machine.Pin.OUT)
NUM_LEDS = 16
PIN_NUM = 6
brightness = 0.2


# Configure the number of WS2812 LEDs.
NUM_LEDS = 10

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1] 
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1] 
    jmp("bitloop")          .side(1)    [T2 - 1] 
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    
# Create the StateMachine with the ws2812 program, outputting on Pin(23).ws2812引脚
sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(23))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

def redState():
    for j in range(0, 20): 
        for i in range(NUM_LEDS): 
            ar[i] = j<<8 
    sm.put(ar,8) 
    time.sleep_ms(50)
    
def greenState():
    for j in range(0, 20): 
        for i in range(NUM_LEDS): 
            ar[i] = j<<16 
    sm.put(ar,8) 
    time.sleep_ms(50)

def blueState():
    for j in range(0, 100): 
        for i in range(NUM_LEDS): 
            ar[i] = j 
    sm.put(ar,8) 
    time.sleep_ms(50)

def blackState():
    for j in range(0, 100):
        for i in range(NUM_LEDS): 
            ar[i] = j<<16 + j<<8 + j 
    sm.put(ar,8) 
    time.sleep_ms(50)
    
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COFFEE = (255, 71, 0)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE, COFFEE)

"""
print("fills")
for color in COLORS:       
    pixels_fill(color)
    pixels_show()
    time.sleep(2)
"""

    
def whiteState():
    pixels_fill(WHITE)
    pixels_show()
    time.sleep(0.2)

def coffeeState():
    pixels_fill(COFFEE)
    pixels_show()
    time.sleep(0.2)
def unavailableState():
    pixels_fill(PURPLE)
    pixels_show()
    time.sleep(0.2)
    pixels_fill(RED)
    pixels_show()
    time.sleep(0.2)
def christmasState():
    pixels_fill(YELLOW)
    pixels_show()
    time.sleep(0.2)
    pixels_fill(GREEN)
    pixels_show()
    time.sleep(0.2)
    pixels_fill(BLUE)
    pixels_show()
    time.sleep(0.2)


    
# while True: 
#     led_onboard.value(1) 
#     utime.sleep(.3) 
#     led_onboard.value(0) 
#     utime.sleep(.3)