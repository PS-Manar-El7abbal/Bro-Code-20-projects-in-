#python calculator

operator=input("Enter an operation (+ - * /)")
num1=float(input("Enter the 1st number :"))
num2=float(input("Enter the 2nd number :"))

if operator=="+":
  result=num1+num2
  print(round(result))
  
elif operator=="-":
     result=num1-num2
     print(round(result))
    
elif operator=="*":
    result=num1*num2
    print(round(result))
elif operator=="/":
   result=num1/num2
   print(round(result,3))
  
else:
    print(f"this operator {operator} is not valid")
