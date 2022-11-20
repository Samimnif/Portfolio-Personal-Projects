from machine import Pin, SPI
import max7219
from boardLED import *
from time import sleep

blackState()
interrupt_flag=0
def callback(pin):
    global interrupt_flag
    interrupt_flag=1

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)
welcome_button = Pin(6, Pin.IN, Pin.PULL_DOWN)
closed_button = Pin(7, Pin.IN, Pin.PULL_DOWN)
back_button = Pin(8, Pin.IN, Pin.PULL_DOWN)

welcome_button.irq(trigger=Pin.IRQ_RISING, handler=callback)
closed_button.irq(trigger=Pin.IRQ_RISING, handler=callback)
back_button.irq(trigger=Pin.IRQ_RISING, handler=callback)



display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(15)
display.fill(0)
display.show()

def welcome():
    global interrupt_flag
    greenState()
    display.fill(0)
    display.brightness(15)
    scrolling_message = "WELCOME"
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        for i in range(3):
            if interrupt_flag == 1:
                interrupt_flag = 0
                display.fill(0)
                return
            sleep(0.01)
        #sleep(0.03)
    for i in range(2):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.5)
    #sleep(1)
    display.fill(0)
    display.text('OPEN',0,0,1)
    display.show()
    for i in range(5):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(1)
    #sleep(5)

def closed():
    global interrupt_flag
    redState()
    display.fill(0)
    display.brightness(5)
    scrolling_message = 'CLOSED'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        for i in range(5):
            if interrupt_flag == 1:
                interrupt_flag = 0
                display.fill(0)
                return
            sleep(0.01)
        #sleep(0.05)
        
def back(i:int):
    global interrupt_flag
    coffeeState()
    display.fill(0)
    display.brightness(15)
    scrolling_message = 'BACK IN '+str(i)+' min'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        for i in range(3):
            if interrupt_flag == 1:
                interrupt_flag = 0
                display.fill(0)
                return
            sleep(0.01)
        #sleep(0.03)
    display_text('TIMS')
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(1)
    #sleep(3)
def display_text(text):
    global interrupt_flag
    display.fill(0)
    display.brightness(15)
    display.text(str(text),0,0,1)
    display.show()

def christmasTree(x):
    display.vline(3+x,0,8,1)
    display.vline(4+x,0,8,1)
    display.hline(0+x,5,8,1)
    display.hline(0+x,6,8,1)
    display.pixel(0+x,5,0)
    display.pixel(7+x,5,0)
    display.hline(0+x,2,8,1)
    display.hline(0+x,3,8,1)
    display.pixel(0+x,3,0)
    display.pixel(7+x,3,0)
    display.pixel(0+x,2,0)
    display.pixel(7+x,2,0)
    display.pixel(1+x,2,0)
    display.pixel(6+x,2,0)
    display.show()
    
def deerText(x):
    display.vline(2+x,0,8,1)
    display.vline(5+x,0,8,1)
    display.hline(0+x,4,8,1)
    display.fill_rect(1+x,3,6,4,1)
    display.line(2+x,7,5+x,7,1)
    display.pixel(1+x,1,1)
    display.pixel(6+x,1,1)
    display.pixel(2+x,4,0)
    display.pixel(5+x,4,0)
    display.line(3+x,6,4+x,6,0)
    
    '''
    display.pixel(0,0,1)
    display.pixel(1,1,1)
    display.hline(0,4,8,1)
    display.vline(4,0,8,1)
    display.line(8, 0, 16, 8, 1)
    display.rect(17,1,6,6,1)
    display.fill_rect(25,1,6,6,1)
    '''
    display.show()

def christmadText():
    global interrupt_flag
    christmasState()
    display.fill(0)
    display.brightness(15)
    display.text('MERY',0,0,1)
    display.show()
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.5)
    display.fill(0)
    display.text('XMAS',0,0,1)
    display.show()
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.5)
    '''
    scrolling_message = 'MERRY CHRISTMAS'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
    '''
    display.fill(0)
    christmasTree(0)
    christmasTree(16)
    deerText(8)
    deerText(24)
    sleep(1)
    display.pixel(10,4,1)
    display.pixel(26,4,1)
    display.pixel(13,4,1)
    display.pixel(29,4,1)
    display.show()
    sleep(0.3)
    display.pixel(10,4,0)
    display.pixel(26,4,0)
    display.pixel(13,4,0)
    display.pixel(29,4,0)
    display.show()
    christmasState()
    sleep(0.5)
    
    
    
def unavailable():
    global interrupt_flag
    unavailableState()
    display.fill(0)
    display.brightness(5)
    scrolling_message = 'UNAVAILABLE'
    length = len(scrolling_message)
    column = (length * 8)
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        for i in range(3):
            if interrupt_flag == 1:
                interrupt_flag = 0
                display.fill(0)
                return
            sleep(0.01)
    unavailableState()
    display_text('7039')
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.2)
    unavailableState()
    display_text(' OR ')
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.2)
    unavailableState()
    display_text('7007')
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.2)
    unavailableState()
    display_text('<<<<')
    for i in range(3):
        if interrupt_flag == 1:
            interrupt_flag = 0
            display.fill(0)
            return
        sleep(0.2)
    unavailableState()
        
            
time_value = [5, 10, 15, 20, 25, 30, 45, 60]
welcome_value = False
closed_value = False
back_value = False
unavailable_value = False
time = 0
duration = 0

while True:
    if welcome_button.value() and closed_button.value():
        unavailable_value = True
        welcome_value = False
        closed_value = False
        back_value = False
    elif closed_button.value() and unavailable_value:
        duration += 1
        whiteState()
        sleep(0.2)
        blackState()
        if duration > 2:
            welcome_value = False
            closed_value = True
            back_value = False
            unavailable_value = False
            #whiteState()
            blackState()
            sleep(0.2)
    elif welcome_button.value() and unavailable_value:
        duration += 1
        whiteState()
        sleep(0.2)
        blackState()
        if duration > 2:
            welcome_value = True
            closed_value = False
            back_value = False
            unavailable_value = False
            #whiteState()
            blackState()
            sleep(0.2)
    elif welcome_button.value() and unavailable_value == False:
        welcome_value = True
        closed_value = False
        back_value = False
        unavailable_value = False
    elif closed_button.value() and closed_value:
        display_text(duration)
        duration += 1
        whiteState()
        sleep(0.5)
        blackState()
        if duration > 5:
            welcome_value = False
            closed_value = False
            back_value = False
            unavailable_value = False
            display_text('OFF')
            #whiteState()
            blackState()
            sleep(2)
    elif closed_button.value() and unavailable_value == False:
        welcome_value = False
        closed_value = True
        back_value = False
        unavailable_value = False
        duration = 0
    elif back_button.value() and back_value:
        time += 1
        if time > 7:
            time -= 7
        display_text(time_value[time])
        whiteState()
        sleep(0.5)
        blackState()
    elif back_button.value():
        time = 0
        welcome_value = False
        closed_value = False
        back_value = True
        unavailable_value = False
    else:
        if welcome_value:
            welcome()
        elif closed_value:
            closed()
        elif back_value:
            if time > 7:
                time -= 7
            back(time_value[time])
        elif unavailable_value:
            unavailable()
        else:
            display.fill(0)
            display.show()
        duration = 0
        
