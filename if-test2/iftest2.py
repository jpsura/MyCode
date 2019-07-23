#!/usr/bin/env python3
ipchk = input("apply and IP address:")  #promts user for input


if ipchk == "192.0.687.1": # if data is added this will prove true
    print("Looks like the IP address was set:" + ipchk + " this is not recommended.")
elif ipchk:
    print("looks like the IP address was set:" + ipchk)
else: # no data at all
    print ("You did not provide input")
