class ListProcessor:
    def __init__(self):
        self.int_list = []

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


class Program:
    @staticmethod
    def main():
        list_processor = ListProcessor()

        size = int(input("Enter the size of the list: "))
        list_processor.input_list(size)

        print(f"\nSum : {list_processor.calculate_sum()}")
        print(f"Last Item : {list_processor.get_last_item()}")
        print(f"List in Reverse Order : {list_processor.reverse_list()}")
        print(f"Does the list contains a five(5) ? {list_processor.contains_5()}")
        print(f"There are {list_processor.count_less_than_5()} integers in the list that are less than 5")
        print(f"Sorted list after removing first and last item : {list_processor.remove_sort()}")


if __name__ == "__main__":
    program = Program()
    program.main()
