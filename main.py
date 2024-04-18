import os # for clearing the console / screen
from Lesson5 import less5_code1, less5_code2, less5_code3, less5_code4, less5_code5

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    print(' =======================================')
    print('|               WELCOME TO              |')
    print('|         COMPILATION OF CODES!         |')
    print('| This program is a compilation of all  |')
    print('|   the codes in Lesson 4 and Lesson 5  |')
    print('|             in the subject            |')
    print('|         Integrative Programming       |')
    print(' =======================================')
    input('\nPress any key to go to the main program...')

def display_main_menu():
    clear_console()
    print(' ======================================')
    print('|              Main Menu               |')
    print(' ======================================')
    print('|     Lesson 4     |      Lesson 5     |')
    print('|       ( A )      |       ( B )       |')
    print('|--------------------------------------|')
    print('|                 Exit                 |')
    print('|                 ( E )                |')
    print(' ======================================')

def display_lesson4_menu():
    print(' ======================================================')
    print('|                    LESSON 4 CODES                    |')
    print(' ======================================================')
    '''
    Pakikumpleto itong menu para sa lesson 4. Bale dapat 6 ang nandito kasi 6 questions.
    Ito yung mga possible na statements per number:
    1. List Manipulation and Slicing
    2. Adding, Finding Index, and Removing Items in the List
    3. List Methods in Use: Append, Insert, Index, Count, Pop, and Remove
    4. Change Value, Add, Remove, Sort and Perform Operation in the List
    5. Factor List Generator: Create a List of Factors from User Input
    6. Removing Repeated Items in the List
    '''

def switch_for_lesson5(choice):
    if choice == 1:
        clear_console()
        less5_code1.main()  # call the first code in lesson 5 if user's choice is 1
    elif choice == 2:
        clear_console()
        less5_code2.Program().main()  # call the second code in lesson 5 if user's choice is 2
    elif choice == 3:
        clear_console()
        less5_code3.Program().main()  # call the third code in lesson 5 if user's choice is 3
    elif choice == 4:
        clear_console()
        less5_code4.Program().main()  # call the fourth code in lesson 5 if user's choice is 4
    elif choice == 5:
        clear_console()
        less5_code5.Program().main()  # call the fifth code in lesson 5 if user's choice is 5
    else:
        print('\nError: Invalid input! Please enter a valid option!')

def display_lesson5_menu():
    while True:
        clear_console()
        print(' ======================================================')
        print('|                    LESSON 5 CODES                    |')
        print(' ======================================================')
        print('| 1. Generate Tuples with Numbers and Their Squares.   |')
        print('| 2. Divisible Tuples from Integer Tuple List.         |')
        print('| 3. Manage Days in Months                             |')
        print('| 4. Manage Products and Prices                        |')
        print('| 5. User Authentication System                        |')
        print('| 6. Go back to the main menu                          |')
        print(' ======================================================')
        ch = input('Enter choice here: ')
        choice = int(ch)
        # validate the user input for choice
        # if the user input for choice is between 1 and 5, call the method that will perform the switch-case-like method
        if choice in range(1, 6):
            switch_for_lesson5(choice)
        elif choice == 6: # if user input for choice is 6, go back to the main menu using break
            break 
        # else, print error message then ask for user input again
        else:
            print('\nError: Invalid input! Please enter a valid choice...')

def main():
    intro() # not sure if sa labas or sa loob ito dapat
    while True:
        display_main_menu()
        ch = input('Enter choice here: ')
        choice = ch.upper()

        if choice == 'A':
            display_lesson4_menu()
        elif choice == 'B':
            display_lesson5_menu()   # display the options for the lesson 5
        elif choice == 'E':
            break # exit the program
        else:
            print('\nError: Invalid input! Please enter a valid option!')
            input('\nPress any key to continue...')

if __name__ == "__main__":
    main()
