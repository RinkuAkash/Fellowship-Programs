from CustomizeMessage_BL import Change

if __name__=="__main__":
    Full_name=str(input("Enter your full name (First Name followed by Last Name) : "))
    ph_no=str(input("Enter your 10 digit phone number : "))
    while(len(ph_no)!=10):
        print("your phone number is invalid")
        ph_no=str(input("Enter your 10 digit phone number : "))
    message=Change(Full_name,ph_no)
    print(message)
