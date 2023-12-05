from functools import partial, reduce, total_ordering


#reduce, partial, wraps (in decorator module tested), total_ordering

def multiply(x, y):
    return x * y

# create a new function that multiplies by 2 (doubles)
dbl = partial(multiply, 2) # This will create a new function, and will set the first param to 2, so the new function will only take one param, and will multiply it by 2.
print(dbl(4))

# create a new function that multiplies by 3 with kwrags
triple = partial(multiply, y=3) # This will create a new function, and will set the second param to 3, so the new function will only take one param, and will multiply it by 3.
print(triple(4))

# partial will basically prefill the params of the function, and will return a new function that takes the rest of the params.

#random factory messing around
def triple_factory(a):
    def double_factory(b):
        def final(c):
            return a * b * c
        return final
    return double_factory

print(triple_factory(2)(3)(4))

#reduce

#reduce is a function that takes a function, and an iterable, and applies the function to the first two elements of the iterable, then applies the function to the result of the previous application, and the next element of the iterable, and so on, until the iterable is exhausted.

items = [1,2,3,4,5]

multiply_result = reduce(lambda x, y: x * y, items) #this will multiply all the items in the list, and return the result.
print(multiply_result)

add_result = reduce(lambda x, y: x + y, items) #this will add all the items in the list, and return the result.
print(add_result)

#total_ordering

#total_ordering is a class decorator, that will add the missing comparison methods to the class, based on the ones that are implemented.

@total_ordering
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __eq__(self, other):
        return ((self.grade, self.age) == (other.grade, other.age))
    
    def __lt__(self, other):
        return ((self.grade, self.age) < (other.grade, other.age))

s1 = Student("John", "A", 15)
s2 = Student("Jane", "B", 12)
s3 = Student("Dave", "B", 10)

print(s1 > s2)
print(s3 < s2)
print(s1 >= s3)
print(s1 != s2)
print(s1 == s1)
print(s1 == s3)

# All the other comparison methods are implemented based on the ones that are implemented, and the @total_ordering decorator.


