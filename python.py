num1 = int(input("Enter the number 1:"))

num2 = int (input("Enter the number 2:"))
operations = input("+,-,*,/")

if operations == "+":
   print(num1 + num2)
elif operations =="-":
   print(num1 - num2)
elif operations =="*":
  print (num1 * num2)
elif operations =="/":
    if num2 == 0:
       print("Cannot divide by zero")
    else:
       print(num1/num2)
    
else:
   print("invalid operation")