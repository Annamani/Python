print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 99
b = 79
if a > b:
  print("a is greater than b")
else:
  print("a is less than b")
print(bool("Hello"))
print(bool(74))
print(bool(3.465))
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("true"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#isinstance() function,
x=495
print(isinstance(x,complex))