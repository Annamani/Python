# Write a program in python which finds a letter in a string
string = input("Enter a long string \n") 
key = input("Enter the letter to search for: \n")
if(key in string):                  
    print("Letter found in string") 
else:
    print("Letter not found in string \n")