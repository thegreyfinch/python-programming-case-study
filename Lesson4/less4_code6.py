'''
Problem: 
    Write a program that removes any repeated items from a list so that each item appears at most once. 
    For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''

# ESTANISLAO:
original_list = [1, 1, 2, 3, 4, 3, 0, 0] 
print("Original List:", original_list)

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Unique List:", unique_list)
