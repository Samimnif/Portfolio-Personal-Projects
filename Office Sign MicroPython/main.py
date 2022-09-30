from machine import Pin, SPI
import max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)
welcome_button = Pin(6, Pin.IN, Pin.PULL_DOWN)
closed_button = Pin(7, Pin.IN, Pin.PULL_DOWN)
back_button = Pin(8, Pin.IN, Pin.PULL_DOWN)

display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(15)
display.fill(0)
display.show()

def welcome():
    display.fill(0)
    display.brightness(15)
    scrolling_message = "WELCOME"
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        sleep(0.03)
    sleep(1)
    display.fill(0)
    display.text('OPEN',0,0,1)
    display.show()
    sleep(5)

def closed():
    display.fill(0)
    display.brightness(5)
    scrolling_message = 'CLOSED'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        sleep(0.05)
        
def back(i:int):
    display.fill(0)
    display.brightness(15)
    scrolling_message = 'BACK IN '+str(i)+' min'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        sleep(0.03)
    display_text('TIMS')
    sleep(3)
def display_text(text):
    display.fill(0)
    display.brightness(15)
    display.text(str(text),0,0,1)
    display.show()
time_value = [5, 10, 15, 20, 25, 30, 45, 60]
welcome_value = False
closed_value = False
back_value = False
time = 0
duration = 0

while True:
    if welcome_button.value():
        welcome_value = True
        closed_value = False
        back_value = False
    elif closed_button.value() and closed_value:
        display_text(duration)
        duration += 1
        sleep(0.5)
        if duration > 5:
            welcome_value = False
            closed_value = False
            back_value = False
            display_text('OFF')
            sleep(2)
    elif closed_button.value():
        welcome_value = False
        closed_value = True
        back_value = False
        duration = 0
    elif back_button.value() and back_value:
        time += 1
        if time > 7:
            time -= 7
        display_text(time_value[time])
        sleep(0.5)
    elif back_button.value():
        time = 0
        welcome_value = False
        closed_value = False
        back_value = True
    else:
        if welcome_value:
            welcome()
        elif closed_value:
            closed()
        elif back_value:
            if time > 7:
                time -= 7
            back(time_value[time])
        else:
            display.fill(0)
            display.show()

    