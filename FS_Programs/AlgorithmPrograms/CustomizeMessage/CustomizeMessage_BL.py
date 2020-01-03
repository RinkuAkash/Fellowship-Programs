import datetime
import re


def Change(Full_name,ph_no):
    first_name=Full_name.split(" ")
    first_name=first_name[0]

    message="Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
    
    date=datetime.datetime.now()
    date=date.strftime("%d/%m/%Y")

    message=re.sub("<<name>>",first_name,message)
    message=re.sub("<<full name>>",Full_name,message)
    message=re.sub("xxxxxxxxxx",ph_no,message)
    message=re.sub("01/01/2016",date,message)
    return message

