from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW
from machine import Pin, SPI
import max7219
from time import sleep

spi = SPI(2, sck=Pin(18),mosi=Pin(26))
cs = Pin(19, Pin.OUT)


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
  rgb.setColorAll(0x00ff00)
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
  
def tim_coffee_sign():
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

def recv_cb(dummy):
  global mac_addr,data,onetime,ssid
  mac_addr, data = now.espnow_recv_str()
  if data == 'open':
    welcome_sign()
  if data == 'close':
    closed_sign()
  if data == 'meeting':
    meeting_sign()
  if data == 'unavailable':
    unavailable_sign()
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
