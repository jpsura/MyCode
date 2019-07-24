#!/usr/bin/env python3
#!/usr/bin/env python3
thisround = 0 #intergar round initiated to 0
while(True):        #sets loop condition
    print('What is the IPv4 adress used to broadcast on a local network? ')
    answer = input()    #collection from user
    thisround = thisround + 1  #increases round count
    if (answer == '255.255.255.255'): #logic check
        print('correct')
        break
    elif (thisround == 3):
        print('Sorry the answer was 255.255.255.255')
        break
    else:
        print('Sorry, try again')

