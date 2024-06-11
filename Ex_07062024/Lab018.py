# Strings
# Bunch of char
# '',  "", ''', """
name = "Amit"
print(name)
name  = 'Amit'
print(name)
name = """ Amit, is a good boy
He loves to walk alone
....
.....
......"""
print(name)

# Raw String
# r -> By placing r, we can print the string as it is.
dir = r"C:\Users\Amit\Desktop\Python\Python-Learning\Python-Basics"
print(dir)

# Formatted String - f" "
first_name = "Amit"
last_name = "Kumar"
print(first_name + " " + last_name)
print(first_name, last_name)
# f -> By placing f, we can replace the values of the variables in the string.
# {} -> Place holder for the varaibles
print(f"My name is {first_name} {last_name}")
