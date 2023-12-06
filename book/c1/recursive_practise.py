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


def fib(n, memo={}): #with memoization -> since each call splits the tree, this actually makes a difference
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result

#note memoization does nothing if we have recursion without splitting the tree, like in the case of factorial.
    