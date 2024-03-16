#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Declare last digit
if number < 0:
    ldigit = number % -10
else:
    ldigit = number % 10
# Check if last digit is greater than 5
if ldigit > 5:
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
# Check if its 0
elif ldigit == 0:
    print(f"Last digit of {number} is {ldigit} and is 0")
# Check if its not zero and less than 6
elif ldigit < 6 and ldigit != 0:
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
