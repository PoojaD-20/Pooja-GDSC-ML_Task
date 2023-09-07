import string
num1=int(input("Enter the value for num1: "))
num2=int(input("Enter the value for num2: "))
op=input("Enter the operand: ")
if not type(op) is string:
   raise Exception("Invalid Input!!")
if(op=='+'):
    print(num1 + num2)
elif(op=='-'):
    print(num1 - num2)
elif(op=='*'):
    print(num1 * num2)
elif(op=='/'):
    try:
      print(num1/num2)
    except:
      print("division by zero")   
else:
   print("Invalid operator!!")               