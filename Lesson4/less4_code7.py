Problem: 
Write a program that asks the user to enter size of list and input a list of integers. Do the following:’ 
a. Print the sum of items in the list. 
b. Print the last item in the list. 
c. Print the list in reverse order. 
d. Print Yes if the list contains a 5 and No otherwise. 
e. Print how many integers in the list are less than 5. 
f. Remove the first and last items from the list, sort the remaining items, and print the result.

SOURCE CODE
# Ask the user for the size of the list
size = int(input("Enter the size of the list: "))

# Input the list of integers from the user
my_list = []
for i in range(size):
    my_list.append(int(input("Enter integer {}: ".format(i+1))))

# a. Print the sum of items in the list
print("Sum of items:", sum(my_list))

# b. Print the last item in the list
print("Last item:", my_list[-1])

# c. Print the list in reverse order
print("Reversed list:", my_list[::-1])

# d. Print Yes if the list contains a 5 and No otherwise
if 5 in my_list:
    print("Yes")
else:
    print("No")

# e. Print how many integers in the list are less than 5
print("Integers less than 5:", sum(1 for num in my_list if num < 5))

# f. Remove the first and last items, sort the remaining items, and print the result
sorted_list = sorted(my_list[1:-1])
print("Sorted list after removing first and last items:", sorted_list)

SOLANO:
Write a program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

# Function to remove repeated items from a list
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example list
original_list = [1, 1, 2, 3, 4, 3, 0, 0]

# Remove duplicates
unique_list = remove_duplicates(original_list)

# Print the unique list
print("Original list:", original_list)
print("List with duplicates removed:", unique_list)

def remove_duplicates(input_list);
    unique_items = set(input_list)
	result_list = list(unique_items)
    return result_list

def main():
	input_list = [1,1,2,3,4,3,0,0]
	result_list = remove_duplicates(input_list)

print(“Original List: “, input_list)
print(“List after removing duplicates: “, (result_list)

main ()
