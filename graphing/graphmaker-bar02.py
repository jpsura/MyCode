#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 4
    localnetMeans = (20, 35, 30, 35) #LAN length of outage (min)
    wanMeans = (25, 32, 34, 200) #WAN LNEGTH OF OUTAGE (MIN)
    ind = np.arange(N)   #THE X LOCATION OF OUTAGE
    #width of the bars can also be len(x) sequence
    width = 0.35

    #describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    #   stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    #describe the table data
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    ##save graph
    plt.savefig\
     ("/home/student/mycode/graphing/2018summary.png")

main()     

