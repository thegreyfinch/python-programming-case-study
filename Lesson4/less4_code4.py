'''
Start with the list [8,9,10]. Do the following: 
a. Set the second entry (index 1) to 17 
b. Add 4, 5, and 6 to the end of the list 
c. Remove the first entry from the list 
d. Sort the list 
e. Double the list 
f. Insert 25 at index 3 
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''
class ListModifier:
    def __init__(self):
        self.int_list = [8, 9, 10]

    def set_index_item(self, index, number):
        self.int_list[index] = number

    def add_number(self, number):
        self.int_list.extend(number)

    def remove_first_number(self):
        self.int_list.pop(0)

    def sort_list(self):
        self.int_list.sort()

    def double_list(self):
        self.int_list *= 2

    def insert_at_index(self, index, value):
        self.int_list.insert(index, value)

    def go_back_to_lesson4_menu(self):
        input('\nPress any key to go back to the Lesson 4 menu...') 

class Program:
    @staticmethod
    def main():
        list_modifier = ListModifier()

        print(f"Initial List : {list_modifier.int_list}")

        list_modifier.set_index_item(1, 17)
        print(f"A. ] Set index 1 to 17 : {list_modifier.int_list}")
        list_modifier.add_number([4, 5, 6])
        print(f"B. ] Append Numbers : {list_modifier.int_list}")
        list_modifier.remove_first_number()
        print(f"C. ] Remove First Number : {list_modifier.int_list}")
        list_modifier.sort_list()
        print(f"C. ] Sort List : {list_modifier.int_list}")
        list_modifier.double_list()
        print(f"D. ] Double List : {list_modifier.int_list}")
        list_modifier.insert_at_index(3, 25)
        print(f"E. ] Insert 25 at index 3 : {list_modifier.int_list}")

        list_modifier.go_back_to_lesson4_menu()

if __name__ == "__main__":
    program = Program()
    program.main()
