Write a program that asks the user to enter size of list and input a list of integers. Do the following:'  
A.	Print the sum of items in the list. 
B.	Print the last item in the list. 
C.	Print the list in reverse order. 
D.	Print Yes if the list contains a 5 and No otherwise. 
E.	Print how many integers in the list are less than 5. 
F.	Remove the first and last items from the list, sort the remaining items, and print the result.

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
