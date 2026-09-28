num1=float(input("enter number 1:"))
operator=input("enter operator:")
num2=float(input("enter number 2:"))
if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="//":
    result=num1//num2
elif operator=="%":
    result=num1%num2
else:
    result="invalid operator"
print("Result:",result)
