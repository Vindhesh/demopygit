# def sum(a, b):
#     c = a + b
#     return c

# x = sum(3, 4)
# print("x is", x)
# y = sum(5, 7)
# print("y is ", y)

# def odd_even(num):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")

# odd_even(12)
# odd_even(13)


# def fact(n):
#     prod = 1
#     while n>=1:
#         prod = prod * n
#         n -=1
#     return prod

# for i in range(1, 11):
#     print("factorial of ", i ,"is ", fact(i))

def prime(n):
    for i in range (n, 1, -1):
        if n % i == 0:
            print("It is not a prime number")
            print(i)
        else:
            print("it is a prime number")
            print(i)
    return n

x = prime(12)


