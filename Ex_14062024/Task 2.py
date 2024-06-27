# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).

# Take input for side lengths
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check for valid triangle inequality
if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
    print("The input lengths do not form a valid triangle.")
else:
    # Check for equilateral triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    # Check for isosceles triangle
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles.")
    # Otherwise, it's a scalene triangle
    else:
        print("The triangle is scalene.")