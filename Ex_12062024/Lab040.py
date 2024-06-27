# Multiple Condition

# WAP to find the Max between 3 numbers

# Possible Conditions

# num1, num2 , num3

# num1 > num2 and num1 > num3 ->  num1

# num2 > num1 and num2 > num3 -> num2

# num3

# if, elif, else - Order for Conditions

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

# max()

# Ternary Operator
# outTrue if conditin else outfalse
#elif will not be present in ternary operator
# a = 10 if 10 > 5 else 5
# print(a)

# a = 10 if 10 > 5 else 5
# print(a)
# a = 10 if 10 > 5 else 5