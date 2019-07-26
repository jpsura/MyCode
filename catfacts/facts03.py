#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    #the catfact is our interable - take on values found inside
    #r.json()["all"]
    # from the dictionary, print the specific text 

    for catfact in r.json()["all"]:
        print(catfact.get("text")) # the .get returns none if keys not found

main()
