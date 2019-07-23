#!/usr/bin/evn python3

## dictionary is 
mice = {"number": 2, "names": [{"name": "Pinky", "tag": "the real genius"}, {"name": "The Brain", "tag": "insane one"}], "world_domination_status": "pending"}

print(mice['names'][0]["name"])
print(" is ")
print(mice['names'][0]["tag"])
print(mice['names'][1]["name"])
print(" is the  ")
print(mice['names'][1]["tag"])

