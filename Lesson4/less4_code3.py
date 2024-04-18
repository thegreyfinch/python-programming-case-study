'''
Problem:
    Write a program that asks the user to enter size of list and input a list of integers. Do the following:'  
    A.	Print the sum of items in the list. 
    B.	Print the last item in the list. 
    C.	Print the list in reverse order. 
    D.	Print Yes if the list contains a 5 and No otherwise. 
    E.	Print how many integers in the list are less than 5. 
    F.	Remove the first and last items from the list, sort the remaining items, and print the result.
'''

# ESTANISLAO:
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


# SOLANO:
# Function to remove first and last items, sort remaining items, and print the result
def remove_first_last_sort(lst):
    if len(lst) < 3:
        print("List is too short to remove first and last items.")
        return
    lst.pop(0)  # Remove first item
    lst.pop(-1)  # Remove last item
    lst.sort()  # Sort the remaining items
    print("Sorted list after removing first and last items:", lst)

# Main program
def main():
    # Ask the user to enter the size of the list
    size = int(input("Enter the size of the list: "))

    # Input the list of integers
    lst = []
    for i in range(size):
        num = int(input(f"Enter integer {i + 1}: "))
        lst.append(num)

    # A. Print the sum of items in the list
    print("Sum of items in the list:", sum(lst))

    # B. Print the last item in the list
    print("Last item in the list:", lst[-1])

    # C. Print the list in reverse order
    print("List in reverse order:", lst[::-1])

    # D. Print Yes if the list contains a 5 and No otherwise
    if 5 in lst:
        print("D.Yes")
    else:
        print("D. No")

    # E. Print how many integers in the list are less than 5
    less_than_5 = sum(1 for item in lst if item < 5)
    print("Number of integers less than 5:", less_than_5)

    # F. Remove the first and last items from the list, sort the remaining items, and print the result
    remove_first_last_sort(lst.copy())  # Use a copy of the list to preserve the original list

# Call the main function directly
main()
