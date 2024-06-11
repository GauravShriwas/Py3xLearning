# List - Shopping List
# milk, bread, butter, eggs
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_list = ["milk", "bread", "butter", "eggs"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("rice") # add item in the end of the list
print(shopping_list)
shopping_list.insert(0, "sugar") # add item at the specific index
print(shopping_list)

shopping_list.extend(["salt", "chips"]) # add multiple items in the end
print(shopping_list)

shopping_list.remove("eggs") # remove item from the list
print(shopping_list)

shopping_list.pop() # remove last item from the list
print(shopping_list)

shopping_list.index("milk") # get index of item
print(shopping_list)

shopping_list.reverse() # reverse the list
print(shopping_list)

shopping_list.sort() # sort the list alphabetically
print(shopping_list)

# It is mutable in nature.
shopping_list[0] = "cake"
print(shopping_list)


my_list = [1, 2, 3, 4, True, 3.14, "Gaurav"]
print(type(my_list)) # <class 'list'>

