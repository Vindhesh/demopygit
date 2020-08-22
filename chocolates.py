amount = int(input("Enter your amount: "))
chocolate = 1
amount_total = amount * chocolate
print(f"For {amount} you will get {amount_total} chocolates")

wrapper_for_chocolates= 4
total_chocolates = amount_total/wrapper_for_chocolates
total = int(0)
if total_chocolates>int(4):
    total += total_chocolates
    total_chocolates = amount_total/wrapper_for_chocolates
    
else: 
    total += total_chocolates
    total_chocolates = amount_total/wrapper_for_chocolates

total = amount_total + total_chocolates
print(total)