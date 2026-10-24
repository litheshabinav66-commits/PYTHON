num1=int(input("Enter first number"))
num2=int(input("Enter 2nd number"))
num3=int(input("Enter 3rd number"))
if num1>num2 and num2>num3:
    print("num1 is biigest",num1)
elif num2>num1 and num3>num1:
    print(num2)
else:
    print(num3)
