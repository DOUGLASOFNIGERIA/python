
name = "cyberhawk"
user_input = input("Enter the name: ")

try:

	if name == user_input:
		print(f"The {name} is the same as {user_input}")

	else:
		print(f"The {name} is not the same as {user_input}")

except ValueError:
	print("Error: You entered invalid input")