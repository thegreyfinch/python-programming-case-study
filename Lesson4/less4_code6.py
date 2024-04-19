'''
Problem: 
    Write a program that removes any repeated items from a list so that each item appears at most once. 
    For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''
class ListCleaner:
    def __init__(self, input_list):
        self.input_list = input_list
        self.clean_list = []

    def remove_duplicates(self):
        for x in self.input_list:
            if x not in self.clean_list:
                self.clean_list.append(x)

    def get_clean_list(self):
        return self.clean_list

    def display_clean_list(self):
        print(f"Clean List : {self.clean_list}")

    def go_back_to_lesson4_menu():
        input('\nPress any key to go back to the Lesson 4 menu...') 


class Program:
    @staticmethod
    def main():
        int_list = [1, 1, 2, 3, 4, 3, 0, 0]
        list_cleaner = ListCleaner(int_list)
        list_cleaner.remove_duplicates()
        list_cleaner.display_clean_list()
        list_cleaner.go_back_to_lesson4_menu()


if __name__ == "__main__":
    program = Program()
    program.main()
