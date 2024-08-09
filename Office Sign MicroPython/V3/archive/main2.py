from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW
from machine import Pin, SPI
import max7219
from time import sleep

spi = SPI(2, sck=Pin(18),mosi=Pin(26))
cs = Pin(19, Pin.OUT)

interrupt_flag=0
def callback(pin):
    global interrupt_flag
    interrupt_flag=1

welcome_button = Pin(36, Pin.IN, Pin.PULL_DOWN)
closed_button = Pin(21, Pin.IN, Pin.PULL_DOWN)
back_button = Pin(22, Pin.IN, Pin.PULL_DOWN)

welcome_button.irq(trigger=Pin.IRQ_RISING, handler=callback)
closed_button.irq(trigger=Pin.IRQ_RISING, handler=callback)
back_button.irq(trigger=Pin.IRQ_RISING, handler=callback)

display = max7219.Matrix8x8(spi, cs, 4)

rgb.setColorAll(0xFFFFFF)
display.brightness(15)
display.fill(0)
display.show()

def display_text(text):
    global interrupt_flag
    display.fill(0)
    display.brightness(15)
    display.text(str(text),0,0,1)
    display.show()

#Start-Up Boot animation
for i in range(8):
  for n in range(8*4):
    display.fill(0)
    display.show()
    
    display.pixel(n,i,1)
    display.pixel(8*4-n-1,8-i-1,1)
    display.show()

display_text("^SM^")

def welcome_sign():
  print("welcome")
  global interrupt_flag
  rgb.setColorAll(0x00FF00)
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
  
def tim_coffee_sign(i:int):
  print("coffee")
  rgb.setColorAll(0xFF7C00)
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
  sleep(1)

def closed_sign():
  print("closed")
  rgb.setColorAll(0xff0000)
  global interrupt_flag
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
      
def meeting_sign():
  print("meeting")
  rgb.setColorAll(0x9700FF)
  display.fill(0)
  display.brightness(15)
  scrolling_message = 'MEETING IN PROGRESS'
  length = len(scrolling_message)
  column = (length * 8)
  for x in range(32, -column, -1):     
    display.fill(0)
    display.text(scrolling_message ,x,0,1)
    display.show()
    sleep(0.03)
  display_text('\\\\\\\\')
  sleep(1.25)
  
def unavailable_sign():
  print("unavailable")
  rgb.setColorAll(0x0013FF)
  display.fill(0)
  display.brightness(5)
  scrolling_message = 'UNAVAILABLE'
  length = len(scrolling_message)
  column = (length * 8)
  for x in range(32, -column, -1):     
      display.fill(0)
      display.text(scrolling_message ,x,0,1)
      display.show()
      sleep(0.03)
  
  display_text('7039')
  sleep(1.25)
  
  display_text(' OR ')
  sleep(1)
  
  display_text('7066')
  sleep(1.25)

  display_text('<<<<')
  sleep(1)


mac_addr = None
data = None
onetime = None
ssid = None

now = M5ESPNOW()

time_value = [5, 10, 15, 20, 25, 30, 45, 60]
welcome_value = False
closed_value = False
back_value = False
unavailable_value = False
time = 0
duration = 0

def recv_cb(dummy):
  global mac_addr,data,onetime,ssid,interrupt_flag,welcome_value,closed_value,back_value,unavailable_value
  mac_addr, data = now.espnow_recv_str()
  print("received ",data)
  interrupt_flag = 1
  if data == 'open':
    welcome_value = True
    closed_value = False
    back_value = False
    unavailable_value = False
  if data == 'close':
    welcome_value = False
    closed_value = True
    back_value = False
    unavailable_value = False
  if data == 'meeting':
    meeting_sign()
  if data == 'unavailable':
    unavailable_value = True
    welcome_value = False
    closed_value = False
    back_value = False
  if data == 'tim':
    tim_coffee_sign()
  if onetime:
    now.espnow_add_peer(mac_addr, 1, 1, False)
    now.espnow_recv_cb(recv_cb)
    onetime = 0
  now.espnow_send_data(1, data+'-done')
  pass

now.espnow_init(1, 1)
onetime = 1
ssid = 'OFFICE_REMOTE'
now.espnow_set_ap(ssid, '')
now.espnow_recv_cb(recv_cb)



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
      welcome_sign()
    elif closed_value:
      closed_sign()
    elif back_value:
      if time > 7:
        time -= 7
      tim_coffee_sign(time_value[time])
    elif unavailable_value:
      unavailable_signn()
    else:
      display.fill(0)
      display.show()
    duration = 0



