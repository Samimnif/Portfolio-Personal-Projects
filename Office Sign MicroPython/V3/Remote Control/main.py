from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW
import time
from machine import Pin, I2C
import ssd1306

'''welcome_button =  btn.attach(22)
closed_button = btn.attach(19)
back_button = btn.attach(23)'''
welcome_button = Pin(22, Pin.IN, Pin.PULL_DOWN)
closed_button = Pin(19, Pin.IN, Pin.PULL_DOWN)
back_button = Pin(23, Pin.IN, Pin.PULL_DOWN)

i2c = I2C(0, scl=Pin(21), sda=Pin(25))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('^Controller^', 20, 10)  
oled.text('SM Services', 20, 30) 
oled.text('^V1.0^', 40, 50)   
oled.show()
rgb.setColorAll(0xFFFFFF)
rgb.setBrightness(100)

wait_ms(2500)
rgb.setColorAll(0x0)
oled.fill(0)
oled.text('READY', 40, 30) 
oled.show()



flag_cb = None
slave_mac = None
slave_data = None
run = None
count_send = None
cnt_succes = None
peer_mac = None
slave_ssid = None

now = M5ESPNOW()


peer_mac = None



def send_cb(flag):
  global flag_cb,slave_mac,slave_data,run,count_send,cnt_succes,peer_mac,slave_ssid
  flag_cb = flag
  if flag_cb:
    rgb.setBrightness(100)
    wait_ms(200)
    rgb.setBrightness(10)
    wait_ms(200)
    rgb.setBrightness(100)

  pass




def recv_cb(dummy):
  global flag_cb,slave_mac,slave_data,run,count_send,cnt_succes,peer_mac,slave_ssid
  slave_mac, slave_data = now.espnow_recv_str()
  rgb.setColorAll(0xFFFFFF)
  oled.text('Data Received', 10, 40)  
  oled.show()
  pass



def buttonA_wasPressed():
  global flag_cb, slave_mac, slave_data, run, count_send, cnt_succes, peer_mac, slave_ssid
  run = 1
  rgb.setColorAll(0x9700FF)
  now.espnow_send_data(1, 'meeting')
  oled.fill(0)
  oled.text('Sent Meeting', 10, 10)  
  oled.show()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonA_wasDoublePressed():
  global flag_cb, slave_mac, slave_data, run, count_send, cnt_succes, peer_mac, slave_ssid
  run = 1
  rgb.setColorAll(0x0013FF)
  now.espnow_send_data(1, 'unavailable')
  oled.fill(0)
  oled.text('Sent Unavail', 10, 10)  
  oled.show()
  pass
btnA.wasDoublePress(buttonA_wasDoublePressed)

#def buttonA_pressFor():
#  global flag_cb, slave_mac, slave_data, run, count_send, cnt_succes, peer_mac, slave_ssid
#  run = 1
#  rgb.setColorAll(0x993399)
#  now.espnow_send_data(1, 'meeting')
#  pass
#btnA.pressFor(0.8, buttonA_pressFor)


now.espnow_init(1, 1)
count_send = 0
cnt_succes = 0
flag_cb = 0
run = 0
slave_ssid = 'OFFICE_REMOTE'
while peer_mac == None:
  peer_mac = now.espnow_scan(1, slave_ssid)
now.espnow_add_peer(peer_mac, 1, 0, False)
now.espnow_send_cb(send_cb)
now.espnow_recv_cb(recv_cb)

while True:
  if welcome_button.value():
    now.espnow_send_data(1, 'open')
    rgb.setColorAll(0x00FF00)
    oled.fill(0)
    oled.text('Sent Open', 10, 10)  
    oled.show()
    pass
  elif closed_button.value():
    now.espnow_send_data(1, 'close')
    rgb.setColorAll(0xff0000)
    oled.fill(0)
    oled.text('Sent Close', 10, 10)  
    oled.show()
    pass
  elif back_button.value():
    now.espnow_send_data(1, 'tim')
    rgb.setColorAll(0xFF7C00)
    oled.fill(0)
    oled.text('Sent Tim', 10, 10)  
    oled.show()
    pass
    
