# For loop
for counter in range(0, 101, 2):  # Even
    print(counter)

for counter in range(1, 101, 2):  # Odd
    print(counter)

for counter in range(1, 101):  # Odd
    print(counter)
    if counter == 5:
        break

print("Outside of the program")

