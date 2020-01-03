import datetime
entry=input("Enter 1 to start stopwatch :")
if entry=='1':
    start=datetime.datetime.now()
    while(entry!='0'):
        entry=input("Enter 0 to end stopwatch : ")
        if entry!=0:
            print("Invalid input")
    print("Elapsed time: ",datetime.datetime.now()-start)

