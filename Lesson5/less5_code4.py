'''
Problem:
    Write a program that repeatedly asks the user to enter product names and prices. 
    Store all of these in a dictionary whose keys are the product names and whose values are the prices. 
    When the user is done entering products and prices, allow them to repeatedly enter a product name and 
    print the corresponding price or a message if the product is not in the dictionary. 
'''
VARGAS:
class Products:
    def __init__(self):
        self.product_info = {} # dictionary that will contain product name and product price pair
        self.product_names = None # a list that stores the product names
    
    def get_input_for_prod_info(self):
        i = 0 # increment variable to display the nth number of product
        while True:
            print('\nPRODUCT ', i + 1) # displays the nth number of product
            name = input('Enter the name of product: ')
            # continue getting user input for price if the input is invalid or not a number
            while True:
                try:
                    price = float(input('Enter the price of product: '))
                    break
                except ValueError:
                    print('Error: Invalid input! Please enter a number for the product price...\n')
            # add the name and price in the dictionary
            self.product_info.update({name: price}) # add in a dictionary form: inside curly braces and using colon
            # ask the user for another input, if 'n' stop getting input
            ans = input('\nDo you want to add another product? (y / n): ')
            answer = ans.lower()
            if answer == 'n':
                break
            i = i + 1 # increment i by one value to for displaying the current nth number product
    
    def display_products(self):
        print('\nLIST OF PRODUCTS:')
        print(self.product_info)  

    def validate_input_prod_name(self, prod_name):
        # get the keys or the product names in the dictionary using keys()
        self.product_names = self.product_info.keys()
        # iterate over the product names to check if the user input for product name is in the dictionary
        uppercased_prod_name = prod_name.upper() # uppercase the inputted product name for validation
        for name in self.product_names:
            uppercased_name = name.upper() # uppercase the product names inside the dictionary for validation
            # if the uppercased inputted prod name by the user is equal to the uppercased product name in the dictionary, return True
            if uppercased_prod_name == uppercased_name: 
                return True
            else:
                continue
        return False

    def get_price_of_product(self, prod_name):
        # iterate over the product_info dictionary to retrieve the specific price of the user inputted product name
        # first, uppercase the user inputted product name
        uppercased_prod_name = prod_name.upper()
        for (key, value) in self.product_info.items():
            # uppercase the key for validation
            uppercased_key = key.upper()
            if uppercased_prod_name == uppercased_key:
                return value
        return None

    def display_price_per_product(self):
        print('\nGET PRICES OF PRODUCTS!')
        while True:
            try:
                prod_name = input('Enter the name of the product: ')
                # validate user input for product name based on the following conditions:
                is_prod_name_in_dictionary = self.validate_input_prod_name(prod_name) 
                # if the inputted product name by the user is in the keys in the dictionary, retrieve and display the price of the specified product name
                if is_prod_name_in_dictionary:
                    prod_price = self.get_price_of_product(prod_name)
                    print(f'\nThe price of {prod_name} is {prod_price}')
                # else, if the user input for prod_name does not exist in the dictionary, return KeyError then ask for user input again
                else:
                    raise KeyError('\nError: Invalid input! Please enter a valid product name...')
                # ask the user for another product name input
                ans = input('\nDo you want to get the price of another product? (y / n): ')
                answer = ans.lower()
                if answer == 'n':
                    break
            except KeyError as ke:
                print(ke)
    
    def go_back_to_lesson5_menu(self):
        input('\nPress any key to go back to the Lesson 5 menu...')

class Program:
    def main(self):
        my_obj = Products()
        my_obj.get_input_for_prod_info()
        my_obj.display_products()
        my_obj.display_price_per_product()
        my_obj.go_back_to_lesson5_menu()

if __name__ == "__main__":
    program = Program()
    program.main()

SOLANO:
def add_products_to_dictionary():
    # Initialize an empty dictionary to store product names and prices
    products = {}
    while True:
        # Prompt the user to enter a product name or 'done' to finish
        product_name = input("Enter product name (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        # Prompt the user to enter the price of the product
        product_price = float(input("Enter price for {}: $".format(product_name)))
        # Add the product name and price to the dictionary
        products[product_name] = product_price
    return products

def find_product_price(products):
    while True:
        # Prompt the user to enter a product name to find its price or 'quit' to exit
        product_name = input("Enter a product name to find its price (or type 'quit' to exit): ")
        if product_name.lower() == 'quit':
            break
        # Check if the product is in the dictionary
        if product_name in products:
            # Print the price of the product
            print("Price of {}: ${}".format(product_name, products[product_name]))
        else:
            # Print a message if the product is not found
            print("Product '{}' not found.".format(product_name))
def main():
    # Add products and their prices to the dictionary
    products = add_products_to_dictionary()
    # Find product prices based on user input
    find_product_price(products)

# Call the main function to run the program
main()
