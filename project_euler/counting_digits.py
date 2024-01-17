# https://projecteuler.net/problem=156


def count_digits(n, d):
    final = 0
    for digit in range(0, n+1):
        final += sum([1 for x in str(digit) if int(x) == d])
    
    return final


print(count_digits(321, 1))