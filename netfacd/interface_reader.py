#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

def MAC():
    try:
        i = input ("What MAC are you looking for ")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
    except:
        print('Could not collect adapter information')

def IP():
    try:
        i = input ("What IP are you looking for ")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information')
    
for i in netifaces.interfaces():
    print('\n**********Details of Interface - ' + i + '*********')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #print mac
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #print IP
    except:
        print('Could not collect adapter information')

MAC()
IP()
