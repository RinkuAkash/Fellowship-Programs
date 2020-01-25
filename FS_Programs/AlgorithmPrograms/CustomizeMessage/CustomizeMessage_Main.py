import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
from CustomizeMessage_BL import Change

if __name__=="__main__":
    print("Enter your full name (First Name followed by Last Name) : ")
    Full_name=Input.singleString()
    print("Enter your 10 digit phone number : ")
    ph_no=Input.singleString()
    while(len(ph_no)!=10):
        print("your phone number is invalid")
        print("Enter your 10 digit phone number : ")
        ph_no=Input.singleString()
    message=Change(Full_name,ph_no)
    print(message)
