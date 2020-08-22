amount = input("Enter your final amount: ")
a1 = int(amount)
tax = int(0)

if a1 <= 250:
    tax = 45

# elif a1 <= 100000:
#     tax = ((a1*0.01)*0.0018)

# elif a1 > 100000 and  a1 <= 1000000:
#     tax = ((1000 + ((0.005*a1))*0.0018) 

# elif a1 > 1000000:
#     tax = ((5500 + (0.001*a1))*0.0018)

print(f"Your tax amount is : ₹{tax}")