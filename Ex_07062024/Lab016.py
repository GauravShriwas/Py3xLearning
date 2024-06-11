# Take a 2 integer inputs from user and print the sum of them.
# We need to use the input() function to get the user input.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# type conversion - str --> int()
result = int(num1) + int(num2)
print(result)

# + --> int sum operation
# + --> str concatenation operation
# int to str conversion - str()
# str to int conversion - int()
print(type(int(num2)))