#!/usr/bin/env python3
##explore reading a file
configfile = open("vlanconfig.cfg", "r")

##display file to screen .read
configlog = configfile.read()

##break the log across line boundries
configlist = configlog.splitlines()

#display line without \n
print(configlist)


configfile.close()

###Explore read lines
#configfile = open("vlanconfig.cfg", "r")
#configlist = configfile.readlines()
#print(configlist)

##iterate thru configlist
#for x in configlist:
#    print(x)

##Always close
#configfile.close()

