def VANN():

    import time
    from datetime import date 
    from datetime import time 
    from datetime import datetime
    run_time =datetime.now()
    print("The dictionary program is being run at: ", run_time)
    dict= {"Vindhesh": "16-02-1997", "Nikita": "03-03-1998", "Nafeesa":"23-08-1997", "Aditya":"06-10-1997"}
    print(dict)
    if input("Do you want to kick Aditya?: ") == "Yes":
        dict.pop("Aditya")
        print("You have Aditya kicked from the group 'VANN'\n Here is the new group 'VNN'")
        
    print(dict)
    

VANN()