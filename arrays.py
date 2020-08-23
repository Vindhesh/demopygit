from array import *  
# a = array('i', [4, 6, 2, 9])
# print(type(a))
# print("The array elements are: ")
# for element in a:
#     print(element)

# arr = array('u', ['a', 'b', 'c', 'd', 'e'])
# print("The array elements are: ")
# for ch in arr:
#     print(ch)

# from array import *
# arr1 = array('d', [1.5, 2.5, -3.5, 4])
# arr2 = array(arr1.typecode, [a*3 for a in arr1])
# print("The elements of the array are :")
# for a in arr2:
#     print(a)

# n = len(arr2)
# print(f'\n''The length of Array is :', n)

from array import *
x = array('i', [10, 20, 30, 40, 50])
n = len(x)

# for i in range(n):
#     print(x[i], end = ' ')
i = 0
while i<n:
    print(x[i], end= ' ')
    i += 1

y = x[0:2]
print(type(y))
print(y)
