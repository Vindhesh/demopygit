from datetime import datetime
# print(type(datetime.MAXYEAR))
# print(type(datetime.MINYEAR))
# print(type(type))

# print(datetime.datetime.now())
# import time
# print(time.time())
# print(datetime.time.fromtimestamp(time.time()))

now = datetime.date.now()
print(now)
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
years = (age.days/365)
print(years)  