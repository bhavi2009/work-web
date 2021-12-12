num1 = int(input("Enter the first number: "))
sign = input("enter the sign/operation: ")
num2 = int(input("Enter the second number: "))

if sign == '+' :
    print(num1+num2)
elif sign == '-' :
    print(num1-num2)
elif sign == '*' :
    print(num1*num2)
elif sign == '/' :
    print(num1/num2)
else:
    print("Incorrect operation")