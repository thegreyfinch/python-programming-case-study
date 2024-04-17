'''
Problem:
    Write a program that will ask user to input a list of integer tuples. 
    Ask also for another integer value and assign it to K. 
    Output the tuple that are divisible by K.
'''
VARGAS:
class ListOfTuple:
    def __init__(self):
        self.K = None
        self.int_tup_list = [] # list that contains the tuple of integers
        self.div_int_tup_list = [] # list that contains the tuple of integers that are divisible by K

    def get_user_input_for_list(self):
        # get user input for a list of integer tuples
        while True:
            try:
                self.int_tup_list = eval(input('Enter a list of integer tuples (eg., [(1, 2), (3, 4), (5, 6)]): '))
                # validate user input whether it's a list or not
                # if the user input is not a list, raise a ValueError exception
                if not isinstance(self.int_tup_list, list):
                    raise ValueError('Error: Invalid input! Please enter a list...\n')
                # validate user input for the elements inside the list
                for elem in self.int_tup_list:         
                    # if the user input for each element of the list is not a tuple, raise ValueError exception
                    if not isinstance(elem, tuple):
                        raise ValueError("Error: Invalid input! Please enter a tuple of integer/s inside the list...\nIf trying to input a single-valued tuple, please add a comma ',' after the element (eg., [(1,), (2,), (3,)])...\n")
                    
                    # validate user input for the elements inside the tuple
                    else:
                        # if the elements inside the tuple is not integer, raise a ValueError exception
                        for num in elem:
                            if not isinstance(num, int):
                                raise ValueError('Error: Invalid input! Please enter an integer inside the tuple...\n')
                break
            except ValueError as ve:
                print(ve)
            except SyntaxError as se:
                print('Syntax Error: Invalid input. Please enter the accurate value...\n')
            except NameError:
                print('Error: Invalid input. Please enter a list of integer tuples...\n')

    def display_list_of_tup(self):
        # display the list of tuple of integers
        print('\nLIST OF INTEGER TUPLES: ')
        print(self.int_tup_list)

    def get_input_for_k(self):
        print()
        # get user input for the value of K
        while True:
            try:
                self.K = int(input('Enter a value for K: '))
                break
            except ValueError:
                print('Error: Invalid input. Please enter an integer...\n')

    def is_divisible_by_k(self, tup):
        return all(elem % self.K == 0 for elem in tup) # returns 
            

    def display_divisible_tuples(self):
        print(f'\nTUPLES THAT ARE DIVISIBLE BY {self.K}:')
        # iterate for each tuple in the list
        for tup in self.int_tup_list:
            if self.is_divisible_by_k(tup):
                print(tup, end = ' ')
        print()
    
    def go_back_to_lesson5_menu(self):
        input('\nPress any key to go back to the Lesson 5 menu...')

class Program:
    def main(self):
        my_obj = ListOfTuple()
        my_obj.get_user_input_for_list()
        my_obj.display_list_of_tup()
        my_obj.get_input_for_k()
        my_obj.display_divisible_tuples()
        my_obj.go_back_to_lesson5_menu()

if __name__ == "__main__":
    program = Program()
    program.main()

SOLANO:
def filter_tuples_by_divisibility(tuples_list, k):
    # Filter tuples in the list where both elements are divisible by k
    return [tup for tup in tuples_list if tup[0] % k == 0 and tup[1] % k == 0]
def input_tuples():
    tuples_list = []
    while True:
        try:
            # Ask the user to input a tuple of integers separated by commas
            tuple_input = input("Enter a tuple of integers separated by a comma (or type 'done' to finish): ")
            if tuple_input.lower() == 'done':
                break
            # Convert the input string into a tuple of integers and append it to the list
            tuple_values = tuple(map(int, tuple_input.split(',')))
            tuples_list.append(tuple_values)
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")
    return tuples_list

def main():
    # Ask the user to input a list of integer tuples
    tuples_list = input_tuples()
    # Ask the user to input an integer value for k
    k = int(input("Enter an integer value for K: "))
    # Filter tuples divisible by k and print the result
    divisible_tuples = filter_tuples_by_divisibility(tuples_list, k)
    print("Tuples divisible by", k, ":", divisible_tuples)

# Call the main function to run the program
main()


MARIAL:

def input_tuples():
    list_of_tup = []
    number_of_tuples = int(input("Enter the number of tuples you want to input: "))
    for i in range(number_of_tuples):
        number_of_elements = int(input(f"\nEnter the number of elements in tuple {i + 1}: "))
        tuple_elements = []
        for j in range(number_of_elements):
            element = int(input(f"Enter #{j + 1} element of tuple #{i + 1}: "))
            tuple_elements.append(element)
        list_of_tup.append(tuple(tuple_elements))
    return list_of_tup

def all_divisible(tuples_list, k):
    divisible_tuples = []
    for tup in tuples_list:
        all_divisible = True 
        for element in tup:
            if element % k != 0:
                all_divisible = False
                break
        if all_divisible:
            divisible_tuples.append(tup)
    return divisible_tuples

def one_divisible(tuples_list, k):
    divisible_tuples = []
    for tup in tuples_list:
        for element in tup:
            if element % k == 0:
                divisible_tuples.append(tup)
                break
# Main function
def main():
    list_of_tup = input_tuples()
    k = int(input("\nEnter an integer to check divisibility: "))
    divisible_tuples = all_divisible(list_of_tup, k)                #one_divisible(list_of_tup, k)
    print(f"\n\nList of Tuples => {list_of_tup}")
    print(f"\nTuples divisible by {k} => {divisible_tuples}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
