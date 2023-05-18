import os
import subprocess
from dataFetch import *
from epaper_display import *
import threading

roomNo = input('room number:')
jackID = input('jack id:')

proc = subprocess.Popen(["hostname -I"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print("program output:", out)
ip = out
ipAddress = ''
for i in str(ip):
    if i == ' ':
        break
    ipAddress += i
print('IP: ',ipAddress)
os.system("tshark -c 10000 -V cdp -w tsharkScan.pcap")
scanning_d = threading.Thread(target=scanning_page, name="Scanning Page")
scanning_d.start()
os.system('tshark -2 -R "cdp" -r tsharkScan.pcap -T json > output.json')
os.system("tshark -r file -V cdp > output.txt")
data = getData("output.json")
os.system(f'cp output.json {roomNo}.json')
print(data)
if scanning_d.is_alive == False:
    result_display(ipAddress, data)

os.system("sudo ifconfig eth0 up")
os.system("sudo ifconfig eth0 down")
os.system("ethtool eth0 > ethernetStatus.txt")
print(ethActive("ethernetStatus.txt"))
# sudo ifconfig eth0 up
# sudo ifconfig eth0 down
# ethtool eth0

