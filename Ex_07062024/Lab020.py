# Strings
# In Built Function -
# Function -> Repeat a task - You can use a function to repeat a task.
# print(), input(), type(), format(), len(), max(), min(), id(), sum(), avg

# Strings
name = "John" # 0 to 3
# 0, 1, 2, 3
# J, o, h, n
print(name)
print(type(name))
print(len(name))
print(id(name)) # id -> memory address of the string --> 2332398342704
# lenght of strint (1)
#name = name.upper()
#name = name.lower()
name = name.count('J')
print(name)
print(name[4]) # string index out of range


# Strings are immutable in Python - You can't change the string.
name[0] = "P" # TypeError: 'str' object does not support item assignment