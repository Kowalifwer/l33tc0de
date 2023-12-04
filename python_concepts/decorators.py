
def surround_with_prints(func: callable):
    def wrapper(*args, **kwargs):
        if "extra" in kwargs: #showcasing that the decorator can access to all the params passed to the wrapped/decorated function.
            print("WE GOT A CRAZY SETUP HERE") #this functionality comes from the wrapper, but depends on the wrapped params.

        print("Print before")
        val = func(*args, **kwargs)
        print("Print after")
        return val
    
    return wrapper

#wrapping with @
@surround_with_prints
def f1(a):
    print(f"This is {a} function")

def f2(a,b, **kwargs):
    return f"This is {a} {b} function"

f1("CRAZY")

#manual/OG wrapping
f2_wrapped = surround_with_prints(f2) #initialize the wrapper, and pass the function to wrap inside of it
xd = f2_wrapped("one", "two", extra="please") #previously we defined the new function, with the wrapped functionality, that supports the original functions args. Now we can call it
print(xd)


