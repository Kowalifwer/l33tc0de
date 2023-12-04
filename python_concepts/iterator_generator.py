

class PowerTwo:

    def __init__(self, m):
        self.m = m
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1

        if self.current <= self.m:
            return self.current ** 2
        else:
            raise StopIteration


ptwo = PowerTwo(5)

for i in iter(ptwo): #can also be without iter() as that is called directly on any for loop thingy.
    print(i)


# 1. Iterable is an object, which one can iterate over, by using a for loop. Eg. list, tuple, string, dict.
# 2. Iterator is an object, which is used to iterate over an iterable object using __next__() method. This object must implement __iter__() and __next__() methods.
# 2.1 __iter__() method returns the iterator object itself. If required, some initialization can be performed.

# 3. Generator is a function that returns an iterator. It looks like a normal function except that it contains yield statements for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function. 
# Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). 
# When the generator resumes, it picks-up where it left-off (in contrast to functions which start fresh on every invocation).

# 4. Generator Expression is a generator version of list comprehension. It looks like a normal list comprehension except that it returns an iterator instead of a list.
# Example: (x**2 for x in range(10)) is a generator expression which returns a generator that produces values from 0 to 81.

def pow2(n):
    for i in range(n):
        yield 2 ** i
    
    return "Done"

x = pow2(5) #this is already an iterator/generator object. So, no need to call iter() on it.
for i in x:
    print(i)

# next(x) # this will raise StopIteration error as the generator is already exhausted.


iterator = iter([1,2,3,4,5])
for elt in iterator:
    print(elt) #this is calling __next__() method on iterator object.

for elt in iterator:
    print(elt) # this will not print anything as the iterator is already exhausted.

lst = [1,2,3,4,5]

# In Python 3, enumerate, zip, reversed, and a number of other built-in functions return iterators:
z = enumerate(lst)
# so enumerate function returns an iterator object, with __next__() method implemented, returning a tuple of (index, value) pair.
print(z)
print(type(z))
print(next(z))
print(type(next(z))) #this is a tuple

zip_obj = zip(lst, lst)
for i,j in zip_obj:
    print(i,j)

print(zip_obj)
print(type(zip_obj))
print(next(zip_obj))
print(type(next(zip_obj))) #this is a tuple


# >>> enumerate(numbers)
# <enumerate object at 0x7f04384ff678>
# >>> zip(numbers, numbers)
# <zip object at 0x7f043a085cc8>
# >>> reversed(numbers)
# <list_reverseiterator object at 0x7f043a081f28>


##unpacking numbers, i.e a,b,c = (1,2,3) will attempt to run __iter__() method on the tuple object, and then assign the values to a,b,c, via __next__() method.


