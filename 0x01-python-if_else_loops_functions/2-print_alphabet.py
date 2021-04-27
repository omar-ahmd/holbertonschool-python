#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdig = abs(number) % 10
result = "Last digit of {:d} is {:d}".format(number,
                                             lstdig if number > 0
                                             else -(lstdig))
if lstdig > 5:
    result += " and is greater than 5"
elif lstdig == 0:
    result += " and is 0"
else:
    result += " and is less than 6 and not 0"
print(result)
