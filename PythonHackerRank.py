import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1 | ((n >= 6 & n <= 20) & n % 2 == 0):
    print("Weird")
else:
    print("Not Weird")

# second better solution
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# third simplified solution
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

    # python python arithmetic operators
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)

    # python full integer division
    print(a // b)
    # python float (decimal point) division
    print(a / b)

    # python for loop as well as exponent operator **
    for i in range(0, n):
        print(i ** 2)


# python write a function
def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


# python print function
finalString = ""
for i in range(1, n + 1):
    print(finalString + str(i), end="")

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))

a = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(a, x))

# python list comprehension
print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])

a = sorted(map(int, input().split()), reverse=True)
print(a[a.count(a[0])])
