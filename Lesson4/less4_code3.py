class ListProcessor:
    def __init__(self):
        self.int_list = []
    
    def display_title_of_problem(self):
        print('Title: List Methods in Use: Append, Insert, Index, Count, Pop, and Remove')
    
    def display_problem(self):
        print(
'''
Problem:
    Write a program that asks the user to enter size of list and input a list of integers. Do the following: 
        a. Print the sum of items in the list. 
        b. Print the last item in the list. 
        c. Print the list in reverse order. 
        d. Print Yes if the list contains a 5 and No otherwise. 
        e. Print how many integers in the list are less than 5. 
        f. Remove the first and last items from the list, sort the remaining items, and print the result.
'''
        )
        print('Answers: \n')

    def input_list(self, size):
        for i in range(size):
            self.int_list.append(int(input(f"Enter integer {i + 1}: ")))

    def calculate_sum(self):
        return sum(self.int_list)

    def get_last_item(self):
        return self.int_list[-1] if self.int_list else None

    def reverse_list(self):
        return self.int_list[::-1]

    def contains_5(self):
        return "Yes" if 5 in self.int_list else "No"

    def count_less_than_5(self):
        return sum(1 for i in self.int_list if i < 5)

    def remove_sort(self):
        if len(self.int_list) >= 2:
            self.int_list.pop(0)
            self.int_list.pop(-1)
            self.int_list.sort()
        return self.int_list
    
    def go_back_to_lesson4_menu(self):
        input('\nPress any key to go back to the Lesson 4 menu...') 

class Program:
    def main(self):
        list_processor = ListProcessor()
        # Display title and problem
        list_processor.display_title_of_problem()
        list_processor.display_problem()

        size = int(input("Enter the size of the list: "))
        list_processor.input_list(size)

        print(f"\nA. ] Sum : {list_processor.calculate_sum()}")
        print(f"B. ] Last Item : {list_processor.get_last_item()}")
        print(f"C. ] List in Reverse Order : {list_processor.reverse_list()}")
        print(f"D. ] Does the list contains a five(5) ? {list_processor.contains_5()}")
        print(f"E. ] There are {list_processor.count_less_than_5()} integers in the list that are less than 5")
        print(f"F. ] Sorted list after removing first and last item : {list_processor.remove_sort()}")

        list_processor.go_back_to_lesson4_menu()

if __name__ == "__main__":
    program = Program()
    program.main()
