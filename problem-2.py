
#program to find largest in three number-------

num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
num3 = int(input("Enter a third number:"))

if num1 > num2:
    print("This is the largest number:",num1)
elif num2 > num3:
    print("This is the largest number:",num2)
elif num3 > num1:
    print("This is the largest number:",num3)
else:
    print("First Enter three number given above")



