#!/usr/bin/env python3

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## Display parts of the Dictionary
print(switch['hostname'])
print(switch['ip'])

## request a 'fake' key
#print(switch['lynx'])

## Request a 'fake' key with .get() method
print("first test-.get()")
print(switch.get('lynx'))

print("second test-.get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE"))

print("third test-.get()")
print(switch.get('version'))

print("fourth test-.keys()")
print("switch.keys()")

print("fifth test-.values()")
print("switch.values()")

print("sixth test-.pop()")
switch.pop('version') #removes this key (and value) pair
print(switch.keys()) #notice the value of version is gone
print(switch.values()) #notice the value 1.2

print("seventh test-ADD a new value")
switch['adminlogin'] = 'kar108'
print(switch.keys())
print(switch.values())

print("eigth test-ADD a new value")
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())

