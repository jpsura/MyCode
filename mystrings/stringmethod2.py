#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
def main():
    """Run-time code"""
    # create a small sting
    lilstring = "alta3 Research offers classes on python coding"
    newlist = lilstring.split(" ") #returns a list
    print(newlist)

    #create a list of strings
    myiplist = ['192', '168', '0', '12']
    #set single ip as the result of joining the list iplist around the "."
    singleip = ".".join(myiplist)
    #display single ip
    print(singleip)

# Call our main function
main()
