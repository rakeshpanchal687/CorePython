# from Functionsum import *
#
# print(s1)
# print(s2)


def sum_all(a, *varg):
    sum = a
    for n in varg:
        sum += n
        return sum

sum = sum_all(2, 5, 6, 7, 8)
print("sum:", sum)
