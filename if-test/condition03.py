#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## notice how the next line changed
## here we use the lower string method
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
## Always print out to the user
print("Exiting the script")

