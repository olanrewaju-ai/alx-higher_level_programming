#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Declare last digit
lastdigit = int(repr(number)[-1])
# Check if last digit is greater than 5
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastdigit))
# Check if its 0
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))