# this will not work as expected - default value is evaluated on function definition, not on function call.
# so any changes to the default value will be reflected in all the function calls, and the default value will not be reset. on each call.
def test(x = [1,2,3,4]):
    x[2] = "K"

# python suggests to use None as default value, and then check for None in the function body.
def test(x = None):
    if x is None:
        x = [1,2,3,4]
    x[2] = "K"

# test()
# test()



a = 121029380912830129380912830192831029381231212312830123123123123123123123123121203918203918230192301239812
b = 121029380912830129380912830192831029381231212312830123123123123123123123123121203918203918230192301239812

print(a == b)

print(a is b)

# In the case of small strings and some other immutable objects in Python, the interpreter may decide to reuse the same memory location for efficiency. This process is called string interning. So, when you create two string literals with the same value, the interpreter may decide to point both variables to the same memory location to save resources.

# However, this behavior is an implementation detail, and it's not something you should rely on in your code. For larger strings or mutable objects, you might see different behavior with is.

# In general:

# Use == when you want to check if two objects have the same values.
# Use is when you want to check if two variables refer to the exact same object in memory.