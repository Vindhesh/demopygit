#Pelindrome string
s1 = int(input("Enter your number: "))
s2 = ''
for i in s1:
    s2=i+s2
if s1==s2:
    print("Yes, it is a pelindrome.")
else:
    print("No, it is not a pelindrome.")

