#!/usr/bin/env python3

'''Goin down baby'''

#function push commands
def commandpush(devicecmd): #devicecmd == list
    for coffeetime in devicecmd.keys():
        print('handshaking. .. ... connecting with ' + coffeetime)
        # we learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command ---> ' + mycmds, end="\n\n")
            # learns to send commands to devices
#adds reboot notice
def devicereboot(deviceboot):
    for reboot in deviceboot.keys():
        print("Connecting too " + reboot)
        print("REBOOTING NOW GOD DAMNIT")

#start the main script
def main():
    work2do = {"10.0.1.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"]}

    print("welcome to the netwrok device command pusher") # welcome message

    ## get data set to send
    print("\nData set found\n")

    ##run time
    commandpush(work2do) #call the function to push
    devicereboot(work2do)

#call main function
main()
