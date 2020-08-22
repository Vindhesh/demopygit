def Birthday():
    import datetime
    import time
    import pytz
    dict={}
    name=str (input("Enter your name?: "))
    dob= str (input("Enter your date of birth?: "))
    dict.update({name:dob})
    print(f"Thank you for your details {name}!!!")
    print(dict)
    time.sleep(6)

Birthday()
