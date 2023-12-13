a = "123"
b = "123"

c = 1
d = 1

print(c is d) # True
print(a is b) # True

print(id(a) == id(b)) # True
print(id(a) is id(b)) # False