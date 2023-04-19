number=int(input("Enter any number: \n"))
if number%400==0 and number%100==0:
    print("Its a leap year\n")
elif number%4==0 and number%100!=0:
    print("Its a leap year\n")
else:
     print("Its not a leap year\n")