'''
Problem: 
    Write a program that removes any repeated items from a list so that each item appears at most once. 
    For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''

# ESTANISLAO:
# Ask the user for the number of elements in the list
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
my_list = []

# Take input from the user for each element
for i in range(num_elements):
    my_list.append(int(input("Enter element {}: ".format(i + 1))))

# Remove repeated items from the list
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the unique_list
print("Original list:", my_list)
print("List with repeated items removed:", unique_list)
