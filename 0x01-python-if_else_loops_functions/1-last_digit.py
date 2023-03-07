#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    num = number * (-1)
    re = (num % 10) * (-1)
    r = num * (-1)
    if re > 5:
       p = "Last digit of {} is {} and is greater than 5"
    elif re == 0:
       p = "Last digit of {} is {} and is 0"
    elif re < 6:
       p = "Last digit of {} is {} and is less than 6 and not 0"
    print(p.format(r, re))
elif number >= 0:
    rem = number % 10
    if rem > 5:
        n = "Last digit of {} is {} and is greater than 5"
    elif rem == 0:
        n = "Last digit of {} is {} and is 0"
    elif rem < 6:
        n = "Last digit of {} is {} and is less than 6 and not 0"
    print(n.format(number, rem))
