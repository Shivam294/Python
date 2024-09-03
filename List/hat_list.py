hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("Original List: ",hat_list)
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
item = int(input("Enter the new value:"))
hat_list[len(hat_list)//2]= item
print("Updated List: ",hat_list)

# Step 2: write a line of code that removes the last element from the list.
hat_list.remove(hat_list[len(hat_list)-1])
print("\nList after Deletion: ", hat_list)
# Step 3: write a line of code that prints the length of the existing list.

print("\nLength of the List: ",len(hat_list))