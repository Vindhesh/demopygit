import os

# f = open("myfile.txt", 'w')
# str = input("Enter your text: ")
# f.write(str)
# f.close()

# f = open("myfile.txt", 'r')
# str = f.read()
# print(str)

# f.close()

# f = open("myfile.txt", 'w')
# print("Enter text '@' end: ")
# while str != '@':
#     str = input()
#     if (str != '@'):
#         f.write(str + '\n')
# f.close()

f = open("myfile.txt", 'r')

str = f.read().splitlines()
print(str)