'''
Problem:
    Write a program that asks the user for an integer
    and creates a list that consists of the factors of that intege
'''
class FactorFinder:
    def __init__(self):
        self.num = None
        self.factors = []

    def get_integer(self):
        self.num = int(input("Enter an integer: "))

    def find_factors(self):
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                self.factors.append(i)

    def display_factors(self):
        print(f"The factors of {self.num} are {self.factors}")

    def go_back_to_lesson4_menu():
        input('\nPress any key to go back to the Lesson 4 menu...') 

    def find_and_display_factors(self):
        self.get_integer()
        self.find_factors()
        self.display_factors()
        self.go_back_to_lesson4_menu()


class Program:
    @staticmethod
    def main():
        factor_finder = FactorFinder()
        factor_finder.find_and_display_factors()


if __name__ == "__main__":
    program = Program()
    program.main()
