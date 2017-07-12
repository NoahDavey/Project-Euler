# Problem 4 on the project euler website
# Found at: https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_test(number):
    number_str = str(number)
    is_palin = True
    for x in range(len(number_str)/2):
        if number_str[x] == number_str[len(number_str) - 1 - x]:
            is_palin = True
        else:
            is_palin = False
            return is_palin
    return is_palin

potential = 0

for first_num in range(999, 99, -1):
    for second_num in range(999, 99, -1):
        if(palindrome_test(first_num * second_num)):
            if potential <= first_num * second_num:
                print "The first number is", first_num, "and the second number is", second_num
                potential = first_num * second_num

print potential
