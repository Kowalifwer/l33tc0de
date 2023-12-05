
def surround_with_prints(func: callable):
    """Decorator that prints before and after the decorated function"""
    def wrapper(*args, **kwargs):
        if "extra" in kwargs: #showcasing that the decorator can access to all the params passed to the wrapped/decorated function.
            print("WE GOT A CRAZY SETUP HERE") #this functionality comes from the wrapper, but depends on the wrapped params.

        print("Print before")
        val = func(*args, **kwargs)
        print("Print after")
        return val
    
    return wrapper

#wrapping with @
@surround_with_prints #note that the code of the decorator will be executed here! i.e the stuff before def wrapper, and after.
def f1(a):
    print(f"This is {a} function")

def f2(a,b, **kwargs):
    """This is a function that takes two params"""
    return f"This is {a} {b} function"

f1("CRAZY")

#manual/OG wrapping
f2_wrapped = surround_with_prints(f2) #initialize the wrapper, and pass the function to wrap inside of it
xd = f2_wrapped("one", "two", extra="please") #previously we defined the new function, with the wrapped functionality, that supports the original functions args. Now we can call it
print(xd)

print(f2_wrapped.__name__) #this will print wrapper, because the wrapper is the function that is returned by the decorator, and the wrapper is the one that is called when we call the wrapped function.
print(f2_wrapped.__doc__) #this will print None, because the wrapper is the function that is returned by the decorator, and the wrapper is the one that is called when we call the wrapped function.

# to make it work, we need to use functools.wraps
from functools import wraps

def surround_with_prints_wrapped(func: callable):
    """Decorator that prints before and after the decorated function"""
    @wraps(func) #this will copy the metadata from the wrapped function, to the wrapper function.
    def wrapper(*args, **kwargs):
        if "extra" in kwargs: #showcasing that the decorator can access to all the params passed to the wrapped/decorated function.
            print("WE GOT A CRAZY SETUP HERE") #this functionality comes from the wrapper, but depends on the wrapped params.

        print("Print before")
        val = func(*args, **kwargs)
        print("Print after")
        return val
    
    return wrapper

@surround_with_prints_wrapped
def f3(a):
    """This is a function that takes one param"""
    print(f"This is {a} function")

print(f3.__name__) #this will print f3, because the metadata was copied from the wrapped function, to the wrapper function.
print(f3.__doc__) #this will print the docstring of the wrapped function, because the metadata was copied from the wrapped function, to the wrapper function.


