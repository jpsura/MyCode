#!/usr/bin/env python3
from subprocess import call
call(["ip", "link", "show", "up"])
print("This program will check your self before you wreck yourself")
interface = input("Enter your face, like, ens3: ")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

