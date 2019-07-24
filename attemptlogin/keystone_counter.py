#!/usr/bin/env python3
loginfail = 0
loginpass = 0 
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "- - - - -] Authorization failed." in line:
        loginfail += 1 # this is the same as loginpass + 1
        #print("The Number of failed login attempts is" + str(loginfail))
    elif  "-] Authorization failed." in line:
        loginpass += 1
print("The Number of failed login attempts is " + str(loginfail))        
print("The number of passed login attempts is " + str(loginpass))
