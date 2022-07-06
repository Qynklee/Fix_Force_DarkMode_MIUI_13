import os
from time import sleep
from tkinter import Y
print("Check adb devices: \n")

devicesOutput = os.system(".\\adb\\adb.exe devices")
# print(devicesOutput)
print("Continue? (y/n)")
#continue with y 
continueWithY = input()
if continueWithY == "n":
    print("Exiting...")
    exit()

print("Continue!!!\n")

print("Run adb shell pm list packages -3  > packagename.txt", end= "\n")
#run a windows system command
os.system(" .\\adb\\adb.exe shell pm list packages -3  > packagename.txt")

import json

temp = ""

item = {"defaultEnable": False, "overrideEnableValue": 0, "packageName": temp, "showInSettings": True}

item_json = json.dumps(item)

print("Creating JSON object...", end="\n")
print(item_json)

packageList_json = []

print("Creating all app package JSON file ...", end="\n")
#read packagename.txt file line by lin
with open("packagename.txt", "r") as f:
    for line in f:
        # line is in format: "package:packagename"
        # get packagename
        temp = line.split(":")[1].replace("\n", "")
        # print(temp)

        #create item object with packagename
        item = {"defaultEnable": False, "overrideEnableValue": 0, "packageName": temp, "showInSettings": True} 
        

        #append item_json to packageList_json
        packageList_json.append(item)

        # print(json.dumps(packageList_json))

        # print(packageList_json)

        #write packageList_json to file with end line LF
        with open("ForceDarkAppSettings.json", "w") as f:
            f.write(json.dumps(packageList_json, indent=4))

print("Sleep 2s")
sleep(2)
import zipfile

print("Try to zip ForceDarkAppSettings.json")

try:
    srczip = "srcZIP.zip"
    dstzip = "CUSTOM_Fix_Force_Dark_mode_MIUI.zip"
    with zipfile.ZipFile(srczip) as inzip, zipfile.ZipFile(dstzip, "w") as outzip:
        for item in inzip.infolist():
            if item.filename == 'system/etc/ForceDarkAppSettings.json':
                NewContent = open("ForceDarkAppSettings.json", "r").read()
                outzip.writestr(item, NewContent)
            else:
                outzip.writestr(item, inzip.read(item.filename))

    print("zip file success\n")
    print("Copy zip file to device\n")
    print("Install zip by Magisk\n")

except Exception as e:
    print("Error: " + str(e))




