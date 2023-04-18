x = 1
#print("value of x: "+x)  #Gives TypeError: can only concatenate str (not "int") to str
print("value of x: "+format(x))
#passing multiple arguments to format()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#using indexes
quantity = 4
itemno = 967
price = 79.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
txt = "We are the so-called \"Vikings\" from the north."
print(txt)