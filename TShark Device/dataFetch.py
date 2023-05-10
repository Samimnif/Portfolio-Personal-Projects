import json
import re
import textwrap

def getData(fileName):
    a_file = open(fileName, "r")
    json_object = json.load(a_file)
    a_file.close()
    json_object = json_object[0]
    
    data = {"VLAN": None, "Port": None, "LAN": None, "VOIP":None}

    for i in json_object["_source"]["layers"]["cdp"]:
        if i.startswith("Native VLAN:"):
            data["VLAN"] = json_object["_source"]["layers"]["cdp"][str(i)]["cdp.native_vlan"]
        elif i.startswith("Port ID:"):
            data["Port"] = json_object["_source"]["layers"]["cdp"][str(i)]["cdp.portid"]
        elif i.startswith("Device ID:"):
            data["LAN"] = json_object["_source"]["layers"]["cdp"][str(i)]["cdp.deviceid"]
        elif i.startswith("VoIP VLAN Reply:"):
            data["VOIP"] = json_object["_source"]["layers"]["cdp"][str(i)]["cdp.voice_vlan"]
    return data

def ethActive(fileName):
    f = open(fileName, "r")
    for line in f.readlines():
        if "Link detected:" in line:
            match= re.search("no", line)
            if match != None and line[match.start():match.end()] == "no":
                return False
            match= re.search("yes", line)
            if match != None and line[match.start():match.end()] == "yes":
                return True

    f.close()
    return False



if __name__ == "__main__":
    #print(getData())
    print(ethActive("ethernetDOWN.txt"))
    print(ethActive("ethernetUP.txt"))