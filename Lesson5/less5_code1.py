class ListOfTupleGenerator:
    def __init__(self):
        self.num_list = [1, 2, 3] # iniialize the list inside __init__() method
        self.tuple_list = []  # list property that stores the tuples
    
    def display_title_of_problem(self):
        print('Title: Generate Tuples with Numbers and Their Squares.')
    
    def display_problem(self):
        print(
'''
Problem:
    Write a Python program to create a list of tuples having first element as the number and second element as the square of the number. 
    Input: list = [1, 2, 3] Output: [(1, 1), (2, 4), (3, 9)]
'''
        )
        print('Answers: \n')
    
    def generate_list_of_tuples(self):
        for num in self.num_list:
            self.tuple_list.append((num, num**2))
    
    def display_list_of_tuples(self):
        print('List of Tuples: ')
        print(self.tuple_list)
    
    def go_back_to_lesson5_menu(self):
        input('\nPress Enter to go back to the Lesson 5 menu...')

class Program:
    def main(self):
        tuple_generator = ListOfTupleGenerator()
        tuple_generator.display_title_of_problem()
        tuple_generator.display_problem()
        tuple_generator.generate_list_of_tuples()
        tuple_generator.display_list_of_tuples()
        tuple_generator.go_back_to_lesson5_menu()

if __name__ == "__main__":
    program = Program()
    program.main()