#!/usr/bin/env python3
import subprocess ##
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your self before you wreck yourself")
interface = input("Enter your face, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])

