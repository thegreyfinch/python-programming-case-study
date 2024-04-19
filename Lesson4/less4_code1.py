class ListMethods:
    def __init__(self):
        self.x = [1, 2, 3, 4, 5]
        self.y = [11, 12, 13, 14, 15]
        self.z = (21, 22, 23, 24, 25)

    @staticmethod
    def slice_list(lst, start=None, stop=None, step=None):
        if start is None and stop is None and step is None:
            return lst[:]  # Return a copy of the list if no slicing arguments are provided
        else:
            return lst[start:stop:step]

    @staticmethod
    def get_element_at_index(lst, index):
        if -len(lst) <= index < len(lst):
            return lst[index]
        else:
            return None  # Return None for out-of-range indices

    @staticmethod
    def perform_list_operation(x, y, operation):
        if operation == '+':
            return x + y
        elif operation == '-':
            raise TypeError("Unsupported operand type(s) for -: 'list' and 'list'")
        elif operation == '*':
            return x * y
        else:
            return None
        
    @staticmethod
    def go_back_to_lesson4_menu():
        input('\nPress any key to go back to the Lesson 4 menu...') 

class Program:
    @staticmethod
    def main():
        list_methods = ListMethods()  # Instantiate ListMethods to access x, y, and z

        # Accessing x, y, z
        x_list = list_methods.x
        y_list = list_methods.y
        z_tuple = list_methods.z

        # Example operations
        print(f"A. ] 3 * x = {list_methods.perform_list_operation(3, x_list, '*')}")
        print(f"B. ] x + y = {list_methods.perform_list_operation(x_list, y_list, '+')}")
        try:
            print(f"C. ] x - y = {list_methods.perform_list_operation(x_list, y_list, '-')}")  # Unsupported operation
        except TypeError as e:
            print(f"C. ] x - y = Error: {e}")
        # Accessing elements and slicing
        print(f"D. ] Value of x[1] : {list_methods.get_element_at_index(x_list, 1)}")
        print(f"E. ] Value of x[0] : {list_methods.get_element_at_index(x_list, 0)}")
        print(f"F. ] Value of x[-1] : {list_methods.get_element_at_index(x_list, -1)}")
        print(f"G. ] Value of x[:] : {list_methods.slice_list(x_list)}")
        print(f"H. ] Value of x[2:4] : {list_methods.slice_list(x_list, 2, 4)}")
        print(f"I. ] Value of x[1:4:2] : {list_methods.slice_list(x_list, 1, 4, 2)}")
        print(f"J. ] Value of x[:2] : {list_methods.slice_list(x_list, None, 2)}")
        print(f"K. ] Value of x[::2] : {list_methods.slice_list(x_list, None, None, 2)}")

        x_list[3] = 8  # Modify x list
        print(f"L. ] Modified x[3] list: {x_list}")

        list_methods.go_back_to_lesson4_menu()


if __name__ == "__main__":
    program = Program()
    program.main()
