def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def pow(x, n):
    if n == 1:
        return x
    else:
        return x * pow(x, n-1)
# O(N) time and

print(factorial(4))
print(pow(3,3))
