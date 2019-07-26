#!/usr/bin/env python3
import pyexcel

#user data
def get_ip_data():
    input_ip = input("\nwhat is the ip address ")
    input_driver = input("What is the driver associated with this device ")
    d = {"IP": input_ip, "driver": input_driver}
    return d
## code is left off but may help to visualize how pyexcel works with data sets
## ip is the first colum, whereas driver is the second colum
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}, {"IP": "172.16.2.20",\
##        "driver": "arista_eos} ]
## pyexcel.save_as(records=mylist, dest_file_name="ip_lists.xls")

#Runtime
mylistdict = [] #this is the list we turn into xls fil

print("Hello, this program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) #add an item to the list returned by get_ip_data()
    keep_going = input("\nWould you like to add another value? Enter to continue, q to quit")
    if (keep_going.lower() == 'q'):
        break
filename = input("\nWhat is the name of the *xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=(f'{filename}' + ".xls"))

print("The file " + filename + ".xls should be in your local directory")
