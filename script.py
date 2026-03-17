# Script that accepts user input and performs a calculation
name = input("Enter your name: ")

if name == "":
    print("Name cannot be empty")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("\n----- Result -----")
print(f"Hello {name}!")
print(f"The sum of {num1} and {num2} is {sum_result}")
print("------------------")
