
import time
user=input("Enter your name: ")
age= input(f"Enter your age {user}: ")
age1= int(age)
print(f"Your age is {age1} years")
age2= (age1*365*86400)
print(f"Hello {user} you have lived for {age2} seconds")
time.sleep(6)
