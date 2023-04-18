x = "Welcome "
def myfunc():
    x = "Hello Welcome " #same variable inside the function
    print(x +" to python programming ")
myfunc()
print(x+ "to programming")      #same variable outside the fuction


def foo(a, b=4, c=6):
    print(a, b, c)
foo(20, c=12)
