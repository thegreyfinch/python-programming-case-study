class ListCleaner:
    def __init__(self, original_list):
        self.original_list = original_list
        self.unique_list = []
    
    def display_title_of_problem(self):
        print('Title: Removing Repeated Items in the List')
    
    def display_problem(self):
        print(
'''
Problem: 
    Write a program that removes any repeated items from a list so that each item appears at most once. 
    For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''
        )
        print('Answers: \n')
    
    def display_original_list(self):
        print(f'Original List: {self.original_list}')

    def remove_duplicates(self):
        for x in self.original_list:
            if x not in self.unique_list:
                self.unique_list.append(x)

    def get_clean_list(self):
        return self.unique_list

    def display_clean_list(self):
        print(f"Unique List : {self.unique_list}")

    def go_back_to_lesson4_menu(self):
        input('\nPress any key to go back to the Lesson 4 menu...') 


class Program:
    @staticmethod
    def main():
        int_list = [1, 1, 2, 3, 4, 3, 0, 0]
        list_cleaner = ListCleaner(int_list)
        # Display title and problem
        list_cleaner.display_title_of_problem()
        list_cleaner.display_problem()
        list_cleaner.remove_duplicates()
        list_cleaner.display_original_list()
        list_cleaner.display_clean_list()
        list_cleaner.go_back_to_lesson4_menu()


if __name__ == "__main__":
    program = Program()
    program.main()
