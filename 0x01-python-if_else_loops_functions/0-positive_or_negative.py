import random
number = random.randint(-10, 10)
if number == 0:
    print("{} is negative".format(number))
elif number >= 1:
    print("{} is positive".format(number))
else:
    print("{} is negative".format(number))
