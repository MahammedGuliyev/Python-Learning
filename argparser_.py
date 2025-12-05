import argparse

arg=argparse.ArgumentParser()
arg.add_argument("number1",help=("Enter first number"))
arg.add_argument("number2",help=("Enter second number"))
arg.add_argument("operation",help=("Enter operation to be performed: add, sub, mul, div")  )
args=arg.parse_args()

num1=int(args.number1)
num2=int(args.number2)
operation=args.operation
result=None

if operation=="add":
    result=num1+num2
elif operation=="sub":
    result=num1-num2   
elif operation=="mul":
    result=num1*num2
elif operation=="div":
    result=num1/num2

print("The result is:",result)
print("Operation performed:",operation)  
print("First number:",num1)
print("Second number:",num2)