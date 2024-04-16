'''
Problem:
    Write a Python program to create a list of tuples having first element as the number and second element as the square of the number. 
    Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]
'''
def main(return_to_menu=None):
    print('Generate Tuples with Numbers and Their Squares.\n')
    num_list = [1, 2, 3]
    tuple_list = []
    for num in num_list:
        tuple_list.append((num, num**2))
    print(tuple_list)

    # prompt the user to go back to the menu for lesson 5
    input('\nPress any key to go back to the menu for Lesson 5...')
    # code to go back to the lesson 5 menu
    if return_to_menu:
        return_to_menu()

if __name__ == "__main__":
    main()