class ListManipulator:
    def __init__(self):
        self.list_items = []
    
    def display_title_of_problem(self):
        print('Title: Adding, Finding Index, and Removing Items in the List')
    
    def display_problem(self):
        print(
'''
Problem:
    Create a list with the following six items: 67, 62.9, “hi”, False, 8, 67, 'apple', 6.5.
    Begin with the empty list shown below, and add 8 statements to add each item, one per item.
    The first four statements should use the append method to append the item to the list,
    and the last four statements should use concatenation

    Starting with the list of the previous exercise, write Python statements to do the following: 
    a. Append “banana” and 67 to the list. 
    b. Insert the value “dog” at position 3. 
    c. Insert the value 909 at the start of the list. 
    d. Find the index of “hi”. 
    e. Count the number of 67s in the list. 
    f. Remove the first occurrence of 67 from the list. 
    g. Remove False from the list using pop and index
'''  
        )
        print('Answers: \n')

    def append_items(self, items):
        self.list_items.append(items)

    def insert_item(self, index, item):
        self.list_items.insert(index, item)

    def concatenate_items(self, items):
        self.list_items = self.list_items + [items]

    def find_index_of_item(self, item):
        return self.list_items.index(item) if item in self.list_items else -1

    def count_item(self, item):
        return self.list_items.count(item)

    def remove_first_occurrence(self, item):
        if item in self.list_items:
            self.list_items.remove(item)

    def remove_false_using_pop(self):
        if False in self.list_items:
            self.list_items.pop(self.list_items.index(False))

    def go_back_to_lesson4_menu(self):  
        input('\nPress any key to go back to the Lesson 4 menu...')

class Program:
    def main(self):
        # Create an instance of the ListManipulator class
        list_manipulator = ListManipulator()
        # Display title and the problem
        list_manipulator.display_title_of_problem()
        list_manipulator.display_problem()

        list_manipulator.append_items(67)
        list_manipulator.append_items(62.9)
        list_manipulator.append_items("hi")
        list_manipulator.append_items(False)
        print(f"A1. ] Appending in List : {list_manipulator.list_items}")

        list_manipulator.concatenate_items(8)
        list_manipulator.concatenate_items(62.9)
        list_manipulator.concatenate_items("hi")
        list_manipulator.concatenate_items(False)
        print(f"A2. ] Concatenation in List : {list_manipulator.list_items}")

        list_manipulator.append_items('banana')
        list_manipulator.append_items(67)
        print(f"B. ] Appending 'banana' and '67' : {list_manipulator.list_items}")
        
        list_manipulator.insert_item(3, 'dog')
        list_manipulator.insert_item(0, 909)
        print(f"C. ] Insert 'dog' and 909 : {list_manipulator.list_items}")

        print(f"D. ] Index of 'hi' : {list_manipulator.find_index_of_item('hi')}")
        
        print(f"E. ] Number of 67s in the list : {list_manipulator.count_item(67)}")
        
        list_manipulator.remove_first_occurrence(67)
        print(f"F. ] Removed first occurrence of 67 : {list_manipulator.list_items}")
        
        list_manipulator.remove_false_using_pop()
        print(f"G. ] Removed False using pop and index : {list_manipulator.list_items}")    

        list_manipulator.go_back_to_lesson4_menu()

if __name__ == "__main__":
    program = Program()
    program.main()
