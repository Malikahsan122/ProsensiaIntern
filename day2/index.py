full_name = input("Enter your full name (first and last name): ")
space_index = full_name.find(' ')
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
print("First Name:", first_name)
print("Last Name:", last_name)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "undefined (division by zero)"

print(f"\nResults:")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {subtract}")
print(f"{num1} * {num2} = {multiply}")
print(f"{num1} / {num2} = {divide}")
