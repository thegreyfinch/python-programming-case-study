'''
Problem:
    Write a Python program to create a list of tuples having first element as the number and second element as the square of the number. 
    Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]
'''

num_list = [1, 2, 3]
tuple_list = []
for num in num_list:
    tuple_list.append((num, num**2))
print(tuple_list)

