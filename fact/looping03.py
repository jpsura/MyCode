#!/usr/bin/env python3
#library allows us to generate uuidvalues
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("generating UUIDS...")

#range is required because the int can not be looped
for rando in range(howmany):
    print( uuid.uuid4() )


