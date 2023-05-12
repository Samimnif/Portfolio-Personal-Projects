#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13b_V4, epd2in13_V3
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13b_V4.EPD()
tt = epd2in13_V3.EPD()
epd.init()
font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
LBlackimage = Image.new('1', (epd.height, epd.width, ), 255)  # 122*250
LRYimage = Image.new('1', (epd.height, epd.width), 255)  # 122*250
newimage = Image.open(os.path.join(picdir, 'sprott.bmp'))
drawry = ImageDraw.Draw(LRYimage)
drawry.text((40, 0), 'SM Solutions ©', font = font24, fill = 0)
LBlackimage.paste(newimage, (50, 20))
epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
time.sleep(2)

def result_display(ip, result):
    epd.clear()
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

    LBlackimage = Image.new('1', (epd.height, epd.width, ), 255)  # 122*250
    LRYimage = Image.new('1', (epd.height, epd.width), 255)  # 122*250
    drawblack = ImageDraw.Draw(LBlackimage)
    drawry = ImageDraw.Draw(LRYimage)
    newimage = Image.open(os.path.join(picdir, 'carleton2.bmp'))
    drawry.text((5, 0), 'Result:', font = font20, fill = 0)
    drawblack.rectangle((0, 0, 70, 21), outline = 0)
    drawblack.text((0, 20), 'IP: ', font = font18, fill = 0)
    drawry.text((30, 20), f'{ip}', font = font20, fill = 0)
    drawblack.text((0, 40), 'VLAN: ', font = font18, fill = 0)
    drawry.text((60, 40), f'{result["VLAN"]}', font = font20, fill = 0)
    drawblack.text((0, 60), f'Port: {result["Port"]}', font = font18, fill = 0)
    drawblack.text((0, 80), f'LAN: {result["LAN"]}', font = font18, fill = 0)
    drawblack.text((0, 100), f'VoIP VLAN: {result["VOIP"]}', font = font18, fill = 0)
    LBlackimage.paste(newimage, (200, 0))
    epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
    epd.sleep()
''' # Just in case, but not useful for now, too much refresh 
def scanning_page():
    epd.clear()
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    LBlackimage = Image.new('1', (epd.height, epd.width, ), 255)  # 122*250
    LRYimage = Image.new('1', (epd.height, epd.width), 255)  # 122*250
    drawblack = ImageDraw.Draw(LBlackimage)
    drawry = ImageDraw.Draw(LRYimage)

    drawry.text((80, 0), 'Scanning', font = font20, fill = 0)
    drawblack.rectangle((0, 50, 249, 80), outline = 0)
    epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
    for t in range(1, 4):
        drawry.rectangle((3, 53, t*82, 77), fill = 0)
        epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
    epd.sleep()
'''
def scanning_page():
    tt.init()
    tt.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    progress = Image.new('1', (epd.height, epd.width), 255)
    progress_draw = ImageDraw.Draw(progress)
    progress_draw.text((80, 0), 'Scanning', font = font24, fill = 0)
    
    tt.displayPartBaseImage(tt.getbuffer(progress))
    progress_draw.rectangle((0, 50, 249, 80), outline = 0)
    for t in range(1, 50): #248
        progress_draw.rectangle((3, 53, t*5, 77), fill = 0)
        tt.displayPartial(tt.getbuffer(progress))

if __name__ == "__main__":
    try:
        result_display('137.172.168.1',{'VLAN': '301', 'Port': 'FiveGigabitEthernet3/0/4', 'LAN': 'NI7083-AS01-9K.net.carleton.ca', 'VOIP': '2224'})
        scanning_page()
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in13b_V4.epdconfig.module_exit()
        exit()
#result_display('137.172.168.1',{'VLAN': '301', 'Port': 'FiveGigabitEthernet3/0/4', 'LAN': 'NI7083-AS01-9K.net.carleton.ca', 'VOIP': '2224'})