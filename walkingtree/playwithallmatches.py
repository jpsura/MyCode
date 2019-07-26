#!/usr/bin/env python3
##script to search all match
import os


##define a function that stops searching on first match
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return result

lookfor = input("what am I looking for? ")
lookwhere = input("what is the path in which I should search? ")

print(find_all(lookfor, lookwhere))
