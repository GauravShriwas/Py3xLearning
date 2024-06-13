# Explain the difference between the = operator and the == operator in Python
# The = operator is used to assign a value to a variable, while the == operator is used to compare two values.
# = (Assignment Operator): The = operator is used to assign a value to a variable.
x = 5 # Assigns the value 5 to the variable x
name = "Gaurav"  # Assigns the string "Gaurav" to the variable name

# Relational Operators : The == operator is used to check if two values are equal.
# It returns boolean value (True or False)

y = 10
print(x == 5)
print(y == 5)
print(x == y)


# What does the ** operator do in Python, and how is it used?
# The ** operator in Python is called the exponent operator or the power operator.
# It is used to raise a number to a power

print(2 ** 3) # Prints 8

# What does the ^ operator do in Python, and in what context is it commonly used?
# Bitwise Operator :
# The ^ operator in Python is used to perform operations on the bits of numbers.
# It returns the result of XOR operation on the two numbers.
# ^ --> also called as cap, carat,or circumflex symbol.

#                     x    y   x^y
#                     0    0   0
#                     0    1   1
#                     1    0   1
#                     1    1   0

x = 10 # 1010
y = 5  # 0101
print(x ^ y) # 0011
