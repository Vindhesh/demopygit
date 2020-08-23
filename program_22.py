# for x in range(1, 11):
#     for y in range (1, 11):
#         # print(x*y, end = ' ')
#         print('{:8}' .format(x*y), end = '')
#     print()



for i in range(1, 11):
    for j in range(1, 11):
        k = i * j
        print('{:8}'.format(k), end = '')
    print()