num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
oper=input("Choose the operation (+, -, /, *): ")
if oper == "+":
	print("The answer is ", int(num1) + int(num2))
elif oper == "-":
	print("The answer is ", int(num1) - int(num2))
elif oper == "/":
	print("The answer is ", int(num1) / int(num2))
else:
	print("The answer is ", int(num1) * int(num2))