'''
Problem:
    Here is a dictionary of the days in the months of the year: 
    days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 
    'September':30, 'October':31, 'November':30, 'December':31} 

    a. Ask the user to enter a month name and use the dictionary to tell them how many days are in the month. 
    b. Print out all of the keys in alphabetical order. 
    c. Print out all of the months with 31 days. 
    d. Print out the (key-value) pairs sorted by the number of days in each month
'''

class DaysPerMonth:
    # initialize the properties inside the __init__()
    def __init__(self):
        self.days = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        }
        self.sorted_months = None # a list property that stores the sorted months
        self.sorted_items = None # a dictionary property that stores the sorted items based on the number of days

    def display_dictionary(self):
        print('DAYS PER MONTH: ')
        print(self.days)
        print() # newline purposes

    def get_input_for_month(self):
        while True:
            try:
                month = input('Enter a month: ')
                # capitalize user input using capitalize() method regardless if the user input for month is uppercase or lowercase
                # this to achieve flexibility and user-friendliness
                capitalized_month = month.capitalize() 
                # validate if the user input for month exists in the dictionary, if not, raise KeyError
                if not self.days.get(capitalized_month):
                    raise KeyError('Error: Invalid input! Please enter a valid key...')
                # use get method to return the value of a key
                days_of_month = self.days.get(capitalized_month)
                if days_of_month:
                    print(f'{capitalized_month} has {days_of_month} days.')
                    break
            except KeyError as ke:
                print(ke)
                print() # newline purposes

    def get_sorted_months(self, months_list):
        return sorted(months_list)

    def sort_month_name(self):
        # use keys() to get the keys or months of the dictionary and store it in the months_list
        months_list = self.days.keys()
        self.sorted_months = self.get_sorted_months(months_list)
        print() # newline purposes
        print('Months In Alphabetical Order: ')
        print(self.sorted_months)
    
    def get_months_with_31_days(self, dict_items):
        # store months with 31 days using list comprehension
        list_of_months = [key for (key, value) in dict_items if value == 31] 
        return list_of_months

    def display_months_with_31_days(self):
        # get the keys and values of the dictionary using items()
        dict_items = self.days.items()
        months_with_31_days = self.get_months_with_31_days(dict_items)
        print('\nMONTHS WITH 31 DAYS: ')
        print(months_with_31_days)

    def display_items_sorted_by_days(self):
        self.sorted_items = sorted(self.days.items(), key=lambda x: x[1])
        print('\nDAYS PER MONTH (Sorted by Days): ')
        print(self.sorted_items)


class Program:
    def main(self):
        my_obj = DaysPerMonth()
        my_obj.display_dictionary()
        my_obj.get_input_for_month()
        my_obj.sort_month_name()
        my_obj.display_months_with_31_days()
        my_obj.display_items_sorted_by_days()

if __name__ == "__main__":
    program = Program()
    program.main()