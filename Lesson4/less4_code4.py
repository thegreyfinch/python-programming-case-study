'''
Problem:
    Start with the list [8,9,10]. Do the following: 
    A.	Set the second entry (index 1) to 17 
    B.	Add 4, 5, and 6 to the end of the list 
    C.	Remove the first entry from the list 
    D.	Sort the list 
    E.	Double the list 
    F.	Insert 25 at index 3 The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''

# SOLANO:
# Start with the list [8, 9, 10]
# Start with the list [8, 9, 10]
my_list = [8, 9, 10]
print("Original List:", my_list)

# A. Set the second entry (index 1) to 17
my_list[1] = 17

# B. Add 4, 5, and 6 to the end of the list
my_list.extend([4, 5, 6])

# C. Remove the first entry from the list
my_list.pop(0)

# D. Sort the list
my_list.sort()

# E. Double the list
my_list *= 2

# F. Insert 25 at index 3
my_list.insert(3, 25)

# Print the final list
print("The final list:", my_list)

# ALOVEROS:

list = [8,9,10]
print("Original List:",list)
list [1] = 17
list.extend ([4,5,6])
list.pop(0)
list.sort()
list.extend(list)
list.insert(3,25)
print("Final list:",list)


# SINDAY
my_list = [8, 9, 10]

my_list[1] = 17

my_list.extend([4, 5, 6])

my_list.pop(0)

my_list.sort()

my_list *= 2

my_list.insert(3, 25)

# Print the final list
print("The final list:", my_list)
