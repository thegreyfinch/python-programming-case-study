'''
Problem:
    Write a Python program to create a list of tuples having first element as the number and second element as the square of the number. 
    Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]
'''
VARGAS:
def go_back_to_lesson5_menu():
    input('\nPress any key to go back to the Lesson 5 menu...')

def main():
    print('Generate Tuples with Numbers and Their Squares.\n')
    num_list = [1, 2, 3]
    tuple_list = []
    for num in num_list:
        tuple_list.append((num, num**2))
    print(tuple_list)

    # prompt the user to go back to the menu for lesson 5
    go_back_to_lesson5_menu()
    

if __name__ == "__main__":
    main()

SOLANO:

def create_tuples_list(input_list):
    # Create a list of tuples where the first element is the number and the second element is its square
    tuples_list = [(num, num ** 2) for num in input_list]
    return tuples_list
# Input list
input_list = [1, 2, 3]
# Create list of tuples
result = create_tuples_list(input_list)
# Print the result
print("Input:", input_list)
print("Output:", result)


MARIAL:

def main:
    list = [1, 2, 3]  # Can be converted to user-input type for flexibility
    list_of_tup =  []
    for i in list:
        list_of_tup.append((i, i ** 2))
    print(f"List of Tuples => {list_of_tup}")

if __name__ == "__main__":
    main()
