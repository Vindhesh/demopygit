
amount = input("Enter your final amount: ")
a1 = int(amount)

if a1 <= 25000:
    tax = 45
    
elif a1 > 25000 and a1 <= 100000:
    tax = (45 + (a1-25000) * (0.01) * (0.18))

elif a1 > 100000 and a1 <= 1000000:
    tax = ((1000 + ((a1-100000) * (0.005)) ) * (0.18))

elif a1 >= 1000000:
    tax = ((5500 + ((a1-1000000) * (0.001)) ) * (0.18))
    
print(f"Your tax amount is : ₹{tax}")