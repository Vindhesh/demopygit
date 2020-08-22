import sys
sum = int(sys.argv[1]) + int(sys.argv[2])
print("sum = ", sum)


import sys
args = sys.argv[1:]
print(args)

sum = 0
for a in args:
    x = int(a)
    if x%2==0:
        sum+=x

print("sum of evens = ", sum)

