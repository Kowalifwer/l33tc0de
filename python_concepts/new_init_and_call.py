class MyClass:
    a = "aaa"
    
    def __call__(self): #simulates the () syntax for MyClass(), by calling __new__ and applying modifications via __init__.
        instance = self.__new__(self.__class__)
        instance.__init__()
        return instance
    
    def __init__(self):
        self.b = "bbb"

#Note that every class, inherits from obj() by default.
#Additionally, when we instantiate a class like MyClass(), we are calling the __call__ method that returns a new instance AND wraps the __init__ method (to modify the instance).
#This means, that although we feel like the new instance only has the attributes and methods defined in __init__ or the class itself, it actually has all the attributes and methods of obj() as well, including __init__ and __new__.

# For that reason, we can continue creating new instances from even existing instances !! which is a bit wild to me.
# We can even do it with the () syntax, but we need to define our __call__ method to do exact thing python does when we use the () syntax - which is to call __new__ and __init__.


# In fact, __init__ acts like an override for any methods and attrbitues at the Class level. any instance can still access the original class stuff, even via .this !!!. since this is still just a reference to the class itself.
a = MyClass()() #creates an individual instance of MyClass

print(MyClass.a)
print(a.a)
print(a.b)
a.a = "modified from instance" ## this acts like an override for the existing instance (similar to __init__), but does not affect the class itself.
MyClass.a = "modified from global instance" #this acts like an override for the whole class
print(MyClass.a)
print(a.a) # will be "modified from instance" because we overrode it at the instance level.

print("B section")
#we can continue creating infinite instances from existing instances, due to the __call__ method, which really acts like the () syntax for MyClass()
b = a()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()

print(b.a) # will be "modified from global instance" because we overrode it at the class level.
print(b.b)
print(a == b) #False

print("C section")
#this also works of course.
c = MyClass()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()

c.a = "modified instance"
c.__class__.a = "modified global class, from accessing class object from an instance"
print(MyClass.a) # will be "modified global class, from accessing class object from an instance"
print(c.a) # will be "modified instance"



