# Problem 3 on the project euler website
# Found at: https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from math import *

num = 600851475143

def is_prime(number):
    counter = 1
    if number <= 3:
        return True
    while counter <= ceil(number/2):
        # If any the number divides by any of the counter numbers it is not prime
        if number / counter % 1 == 0 and counter != number or counter != 1:
            return False
        counter += 1
    return True


for x in range(20):
    print "The number:", x, "is prime" if is_prime(x) == True else "is not prime"
