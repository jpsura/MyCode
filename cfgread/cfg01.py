#!/usr/bin/env python3
##explore reading a file
configfile = open("vlanconfig.cfg", "r")

print(configfile.read())

configfile.close()

###Explore read lines
configfile = open("vlanconfig.cfg", "r")
configlist = configfile.readlines()
print(configlist)

##iterate thru configlist
for x in configlist:
    print(x)

##Always close
configfile.close()
