# To recurse through the calculator use the input_output() method first
def calculator(number1, number2, operation):
	op = operation
	if op ==  "+" or op == "-" or op == "*" or op == "/" or op == "//" or op == "**":
		# Used the try block in case the numbers are not entered properly
		try:
			n1 = float(number1)
			n2 = float(number2)
			if op == "+":
				return (n1+n2)
			elif op == "-":
				return (n1-n2)
			elif op == "*":
				return (n1*n2)
			elif op == "/":
				return (n1/n2)
			elif op == "//":
				return (n1//n2)
			else:
				return (n1**n2)
		except ValueError:
			print("Invalid numbers entered")

	else:
		print("Invalid Op")
		return False

# User needs to call this method first
def input_output():
	n1 = input("Enter first number: ")
	n2 = input("Enter second number: ")
	op = input("Enter the operation: ")

	# User enters the 3 values then we implement the calculator function
	print(calculator(n1, n2, op))
	choice = input("Do you wish to exit, type y or n: ")
	# If User wishes to continue, we call the input_output function to get input
	if choice == 'n':
		input_output()
	if choice == 'y':
		exit();

print(input_output())
