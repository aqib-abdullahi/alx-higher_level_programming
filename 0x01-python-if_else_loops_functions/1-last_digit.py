#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    num = number * (-1)
    re = num % 10
    r = num * (-1)
    if re > 5:
        print("Last digit of {} is {} and is greater than 5".format(r, re))
    elif re == 0:
        print("Last digit of {} is {} and is 0".format(r, re))
    elif re < 6:
        print("Last digit of {} is {} and is less than 6 and not 0".format(r, re))
elif number >= 0:
    rem = number % 10
    if rem > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, rem))
    elif rem == 0:
        print("Last digit of {} is {} and is 0".format(number, rem))
    elif rem < 6:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, rem))
