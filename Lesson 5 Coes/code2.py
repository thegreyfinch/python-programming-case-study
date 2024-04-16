'''
Problem:
    Write a program that will ask user to input a list of integer tuples. 
    Ask also for another integer value and assign it to K. 
    Output the tuple that are divisible by K.
'''

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

class Program:
    def main(self):
        my_obj = ListOfTuple()
        my_obj.get_user_input_for_list()
        my_obj.display_list_of_tup()
        my_obj.get_input_for_k()
        my_obj.display_divisible_tuples()

program = Program()
program.main()

