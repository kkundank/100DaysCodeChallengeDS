"""
Find the greatest common denominator (GCD) of two numbers.
"""


def gcdDem(a,b):
    num = 1
    while num <= min(a,b):
        if a % num == 0 and b % num == 0:
            num += 1
            continue


print(gcdDem(15, 25))