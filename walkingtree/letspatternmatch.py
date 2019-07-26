#!/usr/bin/env python3
##script to search pattern match
import os, fnmatch


##define a function that stops searching on first match
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("what am I looking for? (example: *txt) ")
lookwhere = input("what is the path in which I should search? ")

print(find(lookfor, lookwhere))
