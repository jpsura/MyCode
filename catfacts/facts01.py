#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    #the .json() method will dump a json strink into pythoni data structures.
    # this is much easier than using th urllib.request
    print(r.json())
main()
