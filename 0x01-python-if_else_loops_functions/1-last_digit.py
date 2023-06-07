#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(str(abs(number))[-1])
print(f"Last digit of {number} is {last} and is",end = " ")
if last == 0:
    print("0")
elif last > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
