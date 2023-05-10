import os
import subprocess
from dataFetch import *

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
os.system("tshark -c 10000 -V cdp -w tsharkTest.pcap")
os.system('tshark -2 -R "cdp" -r tsharkTest.pcap -T json > output.json')
os.system("tshark -r file -V cdp > output.txt")
data = getData("output.json")
os.system(f'cp output.json {roomNo}.json')
print(data)

# sudo ifconfig eth0 up
# sudo ifconfig eth0 down
# ethtool eth0

