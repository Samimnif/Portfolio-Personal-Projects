# Adapting the example in https://learn.adafruit.com/adafruit-oled-featherwing/python-usage
# to use with Raspberry Pi Pico and CircuitPython

import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from time import sleep
from analogio import AnalogIn
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

yAxis = AnalogIn(board.A0)
xAxis = AnalogIn(board.A1)
in_min, in_max,out_min,out_max = (0,65000,-5,5)
filter_joystick_deadzone = lambda x: int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) if abs(x - 32768) > 500 else 0

displayio.release_displays()
i2c = busio.I2C (scl=board.GP1, sda=board.GP0, frequency=1000000) # This RPi Pico way to call I2C

display_bus = displayio.I2CDisplay (i2c, device_address = 0x3C) # The address of my Board

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash = displayio.Group()#max_size=10)
display.show(splash)


def selection(num):
    for i in range(len(splash)):
        splash.pop()
    if num == 0:
        color_bitmap = displayio.Bitmap(128, 20, 1) # Full screen white
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White
         
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=17)
        splash.append(bg_sprite)
         
        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(126, 18, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=18)
        splash.append(inner_sprite)
    elif num == 1:
        color_bitmap = displayio.Bitmap(128, 20, 1) # Full screen white
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White
         
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=37)
        splash.append(bg_sprite)
         
        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(126, 18, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=38)
        splash.append(inner_sprite)
    text_area = label.Label(terminalio.FONT, text="Menu:", color=0xFFFF00, x=2, y=5)
    splash.append(text_area)
    text_area1 = label.Label(terminalio.FONT, text="Move Cursor", color=0xFFFF00, x=2, y=25)
    splash.append(text_area1)
    text_area2 = label.Label(terminalio.FONT, text="Turn Off Machine", color=0xFFFF00, x=2, y=45)
    splash.append(text_area2)

def timeSelect(num):
    for i in range(len(splash)):
        splash.pop()
    text_area = label.Label(terminalio.FONT, text="Timer:", color=0xFFFF00, x=2, y=5)
    splash.append(text_area)
    text_area2 = label.Label(terminalio.FONT, text=str(num)+"  min", color=0xFFFF00, x=2, y=25)
    splash.append(text_area2)

def timer(num):
    for i in range(len(splash)):
        splash.pop()
    color_bitmap = displayio.Bitmap(130, 100, 1) # Full screen white
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White
         
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)
         
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(126, 62, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
    splash.append(inner_sprite)
        
    text_area2 = label.Label(terminalio.FONT,scale=2, text=str(num)+"  sec", color=0xFFFF00, x=40, y=30)
    splash.append(text_area2)
    
def done():
    for i in range(len(splash)):
        splash.pop()
    color_bitmap = displayio.Bitmap(130, 100, 1) # Full screen white
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White
         
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)
         
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(126, 62, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
    splash.append(inner_sprite)
        
    text_area2 = label.Label(terminalio.FONT,scale=2, text="Done", color=0xFFFF00, x=40, y=30)
    splash.append(text_area2)

    
oldx = -2
oldy = 2
max_shake_minutes = 240
move_distance = 100
mouse_pause = .5
loop_sleep = .4
menu = True
jiggle = False
shutdown = False

mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

sel = 0
opt = 0
selection(0)

while True:
    x_offset = filter_joystick_deadzone(xAxis.value) * -1 #Invert axis
    y_offset = filter_joystick_deadzone(yAxis.value)
    if menu:
        if y_offset > oldy:
            if opt == 1:
                opt -= 1
            else:
                opt += 1
            selection(opt)
            print("up")
        elif y_offset < oldy:
            if opt == 1:
                opt -= 1
            else:
                opt += 1
            selection(opt)
            print("down")
        elif x_offset > oldx:
            menu = False
            timeSelect(sel)
            print("right")
        elif x_offset < oldx:
            print("left")
    else:
        if y_offset > oldy:
            sel+=1
            timeSelect(sel)
            print("up")
        elif y_offset < oldy:
            if sel > 0:
                sel-=1
            timeSelect(sel)
            print("down")
        elif x_offset > oldx:
            if sel > 0:
                if opt == 0:
                    jiggle = True
                else:
                    shutdown = True
            #selection(opt)
            print("right")
        elif x_offset < oldx:
            menu = True
            selection(opt)
            print("left")
    if jiggle:
        sleep(1)
        print("jiggle")
        jiggle = False
        for i in range(sel*60):
            mouse.move(x=move_distance)
            sleep(mouse_pause)
            mouse.move(x=-1 * move_distance)
            sleep(mouse_pause)
            timer(sel*60-i)
        done()
        sleep(2)
        selection(opt)
    elif shutdown:
        sleep(1)
        print("shutdown")
        shutdown = False
        for i in range(sel*60):
            mouse.move(x=move_distance)
            sleep(mouse_pause)
            mouse.move(x=-1 * move_distance)
            sleep(mouse_pause)
            timer(sel*60-i)
        done()
        print('pressed')
        kbd.press(Keycode.WINDOWS, Keycode.X)
        kbd.release_all()
        kbd.press(Keycode.U)
        kbd.release_all()
        kbd.press(Keycode.U)
        #kbd.press(Keycode.POWER)
        sleep(1)
        print('released')
        kbd.release_all()
        
    
    #oldx = x_offset
    #oldy = y_offset
    sleep(0.3)
    print(x_offset, y_offset)
    #print(xAxis.value,yAxis.value)
    #selection(0)
    #sleep(1)
    #selection(1)
    #sleep(1)
#     timeSelect()
#     sleep(1)

