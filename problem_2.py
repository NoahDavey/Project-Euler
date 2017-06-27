# Problem 1 on the project euler website
# Found at: https://projecteuler.net/problem=2

# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1
# and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.

from math import *

previous_terms = [0, 1]
current_term = 0

even_fib_nums = []

while (current_term < 4000000):
    current_term = previous_terms[0] + previous_terms[1]
    previous_terms[0] = previous_terms[1]
    previous_terms[1] = current_term
    if current_term % 2 == 0:
        even_fib_nums.append(current_term)

print sum(even_fib_nums)
