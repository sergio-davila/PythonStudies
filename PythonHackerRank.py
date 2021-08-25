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
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
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
