#!/usr/bin/env python3
##script to search pattern match
import os 
import fnmatch

EXCLUDE = ["/usr", "/home", "/var"]  ##dont search these


##define a function that stops searching on first match
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the excluse list
            dirs[:] = [] #remove the dir list
            files[:] = [] #remove the file
        for name in files: #always perform the nested loop
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def main():
    lookfor = input("what am I looking for? (example: *txt) ")
    lookwhere = input("what is the path in which I should search? ")
    print("Results: ", (find(lookfor, lookwhere))
