# Find gmail entered is of legit format (clean email)
'''
The username shouldn't start or end with '.'
The username should be between 6 and 30 character
If user name contains more than 8 characters it should contain atleast one alphabet
'''

import re

gmail=input("Enter the Gmail ID: \n")

gmail=gmail.replace(" ", "").strip()
if gmail.endswith("@gmail.com"):
    username=gmail[:-10]
    if not (username.startswith(".") or username.endswith(".")):
        if 30>= len(username) >=6:
            if len(username) >= 8 and re.search("[a-zA-Z]", username):
                print("\n\"",gmail,"\" is a legit Gmail ID")
            else:
                print("Not a legit ID as username: ",username," contains more than 8 characters it should contain atleast one alphabet")
        else:
            print("Not a legit ID as username: ",username," should be between 6 and 30 character")
    else:
        print("Not a legit ID as username: ",username," should start with numbers or alphabets")
else:
    index=gmail.index("@")
    domain=gmail[index:]
    #domain=domain[:-4]
    print("Not a Gmail ID. Maybe from some other Domain which is here ", domain)
