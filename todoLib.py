from pyrf24 import RF24, rf24
from networkLib import *
import os
from glob import glob
import RPi.GPIO as GPIO #importem la llibreria corresponent
#import shutil


L3=27  #GREEN
GPIO.setmode(GPIO.BCM) #establim com es fara referencia als pins de la RPi
GPIO.setup(L3, GPIO.OUT)
On=True

NODE_A1 = b'75369'
NODE_A2 = b'02736'
NODE_B1 = b'53827'
NODE_B2 = b'91684'
NODE_C1 = b'81629'
NODE_C2 = b'63926'

OWN_ADDRESS = NODE_C1 #TODO Change to each address of each team TR


def initializeRadio():
    radio = RF24()
    if not radio.begin(22,0): #TODO: Here the 1st pin cahnegs for each team
        raise OSError("nRF24L01 hardware isn't responding")
    return radio

def readFile(): #TODO Read file from usb, particular for each team
    """
    Read file from usb.
    Return the file in bytes
    """
    if os.path.exists('/dev/sda1'):
        os.system('sudo mount /dev/sda1 /media/rpi/USB')
    elif os.path.exists('/dev/sdb1'):
        os.system('sudo mount /dev/sdb1 /media/rpi/USB')
    elif os.path.exists('/dev/sdc1'):
        os.system('sudo mount /dev/sdc1 /media/rpi/USB')
    elif os.path.exists('/dev/sdd1'):
        os.system('sudo mount /dev/sdd1 /media/rpi/USB')
    for file in glob("/media/rpi/USB/*.txt"):
        continue
    with open(file, 'rb') as transmittedFile:
        file_data = transmittedFile.read()
    os.system('sudo umount /media/rpi/USB')
    return file_data

def saveFile(file_data): #TODO Save file in usb, particular for each team
    """
    Gets file in bytes.
    Save file in usb.
    """
    if os.path.exists('/dev/sda1'):
        os.system('sudo mount /dev/sda1 /media/rpi/USB')
    elif os.path.exists('/dev/sdb1'):
        os.system('sudo mount /dev/sdb1 /media/rpi/USB')
    elif os.path.exists('/dev/sdc1'):
        os.system('sudo mount /dev/sdc1 /media/rpi/USB')
    elif os.path.exists('/dev/sdd1'):
        os.system('sudo mount /dev/sdd1 /media/rpi/USB')
    #shutil.copy("/home/rpi/textfile/MTP-S23-NM-RX.txt", "/media/rpi/USB/")
    with open('/media/rpi/USB/MTP-S23-NM-RX.txt','wb') as file:
        file.write(file_data)
        led_manager(L3,On)
    os.system('sudo umount /media/rpi/USB')
    
def led_manager(led, estat): #funció per a operar els leds, es donen com a inputs el led i l'estat del led (On/Off) per a fer el funcionament d'aquests
    if(estat):
        GPIO.output(led, GPIO.HIGH) #obrir el led
    else:
        GPIO.output(led, GPIO.LOW) #tencar el led
