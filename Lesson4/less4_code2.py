'''
Problem:
    Create a list with the following six items: 67, 62.9, "hi", False, 8, 67, 'apple', 6.5. 
    Begin with the empty list shown below, and add 8 statements to add each item, one per item. 
    The first four statements should use the append method to append the item to the list, and the last four statements should use concatenation.

    Starting with the list of the previous exercise, write Python statements to do the following: 
    A.	Append "banana" and 67 to the list.
    B.	Insert the value "dog" at position 3. 
    C.	Insert the value 909 at the start of the list. 
    D.	Find the index of "hi". 
    E.	Count the number of 67s in the list. 
    F.	Remove the first occurrence of 67 from the list.
    G.	Remove False from the list using pop and index
'''

# SOLANO:
# Starting list
my_list = [67, 62.9, "hi", False, 8, 67, 'apple', 6.5]

# A. Append "banana" and 67 to the list.
my_list.append("banana")
my_list.append(67)

# B. Insert the value "dog" at position 3.
my_list.insert(3, "dog")

# C. Insert the value 909 at the start of the list.
my_list.insert(0, 909)

# D. Find the index of "hi".
index_of_hi = my_list.index("hi")

# E. Count the number of 67s in the list.
count_of_67 = my_list.count(67)

# F. Remove the first occurrence of 67 from the list.
my_list.remove(67)

# G. Remove False from the list using pop and index
index_of_false = my_list.index(False)
my_list.pop(index_of_false)

# Print the modified list
print("Modified list:", my_list)
print("Index of 'hi':", index_of_hi)
print("Count of 67s:", count_of_67)


# ALOVEROS:

list = []
list.append(67)
list.append(62.9)
list.append("Hi")
list.append(False)
list = list + [8]
list =list + [67]
list = list + ["apple"]
list = list + [6.5]
list.append("banana")
list.append(67)
list.insert(3, "dog")
list.insert(0, 909)
print(list)
index_hi = list.index("Hi")
print("Index of 'Hi':", index_hi)
count_67 = list.count(67)
print("Number of Occurences of 67's in the list:", count_67)
list.remove(67)
list.pop(list.index(False))
