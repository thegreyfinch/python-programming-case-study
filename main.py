import os
from colorama import Fore, Style
from Lesson4 import less4_code1, less4_code2, less4_code3, less4_code4, less4_code5, less4_code6
from Lesson5 import less5_code1, less5_code2, less5_code3, less5_code4, less5_code5

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear_console()
    print(Fore.YELLOW + """
   _____ _             _   _            _   _            _     
  / ____(_)           | | (_)          | | (_)          | |    
 | (___  _ _ __   __ _| |_ _  ___ ___  | |_ _  ___  _ __| |__  
  \___ \| | '_ \ / _` | __| |/ __/ _ \ | __| |/ _ \| '__| '_ \ 
  ____) | | | | | (_| | |_| | (_|  __/ | |_| | (_) | |  | |_) |
 |_____/|_|_| |_|\__, |\__|_|\___\___|  \__|_|\___/|_|  |_.__/ 
                   __/ |                                       
                  |___/                                        
""")

    print(Fore.CYAN + 'Welcome to the Compilation of Codes!\n')
    print('This program is a compilation of all the codes in Lesson 4 and Lesson 5')
    print('in the subject of Integrative Programming.\n')
    input('Press Enter to continue to the main program...')

def display_main_menu():
    clear_console()
    print(Fore.GREEN + """
  _______ _                 _            _   _            _     
 |__   __| |               | |          | | (_)          | |    
    | |  | |__   __ _ _ __ | |_ __ _ ___| |_ _  ___  _ __| |__  
    | |  | '_ \ / _` | '_ \| __/ _` / __| __| |/ _ \| '__| '_ \ 
    | |  | | | | (_| | | | | || (_| \__ \ |_| | (_) | |  | |_) |
    |_|  |_| |_|\__,_|_| |_|\__\__,_|___/\__|_|\___/|_|  |_.__/ 
                                                                 
""")
    print('Main Menu:\n')
    print('Select an option:')
    print('  A. Lesson 4')
    print('  B. Lesson 5')
    print('  E. Exit\n')

def switch_for_lesson4(choice):
    if choice == 1:
        clear_console()
        less4_code1.Program().main()
    elif choice == 2:
        clear_console()
        less4_code2.Program().main()
    elif choice == 3:
        clear_console()
        less4_code3.Program().main()
    elif choice == 4:
        clear_console()
        less4_code4.Program().main()
    elif choice == 5:
        clear_console()
        less4_code5.Program().main()
    elif choice == 6:
        clear_console()
        less4_code6.Program().main()
    else:
        print(Fore.RED + '\nError: Invalid input! Please enter a valid option!' + Style.RESET_ALL)

def display_lesson4_menu():
    while True:
        clear_console()
        print(Fore.MAGENTA + """
  _______ _ _        _______          _ 
 |__   __(_) |      |__   __|        | |
    | |   _| |_ ___    | | ___   ___ | |
    | |  | | __/ _ \   | |/ _ \ / _ \| |
    | |  | | ||  __/   | | (_) | (_) | |
    |_|  |_|\__\___|   |_|\___/ \___/|_|
                                        
""")
        print('LESSON 4 CODES:\n')
        print('1. List Manipulation and Slicing')
        print('2. Adding, Finding Index, and Removing Items in the List')
        print('3. List Methods in Use: Append, Insert, Index, Count, Pop, and Remove')
        print('4. Change Value, Add, Remove, Sort and Perform Operation in the List')
        print('5. Factor List Generator: Create a List of Factors from User Input')
        print('6. Removing Repeated Items in the List')
        print('7. Go back to the main menu\n')
        ch = input('Enter choice here: ')
        choice = int(ch)
        if choice in range(1, 7):
            switch_for_lesson4(choice)
        elif choice == 7:
            break
        else:
            print(Fore.RED + '\nError: Invalid input! Please enter a valid choice...' + Style.RESET_ALL)

def switch_for_lesson5(choice):
    if choice == 1:
        clear_console()
        less5_code1.Program().main()
    elif choice == 2:
        clear_console()
        less5_code2.Program().main()
    elif choice == 3:
        clear_console()
        less5_code3.Program().main()
    elif choice == 4:
        clear_console()
        less5_code4.Program().main()
    elif choice == 5:
        clear_console()
        less5_code5.Program().main()
    else:
        print(Fore.RED + '\nError: Invalid input! Please enter a valid option!' + Style.RESET_ALL)

def display_lesson5_menu():
    while True:
        clear_console()
        print(Fore.MAGENTA + """
  _______ _ _        _______          _ 
 |__   __(_) |      |__   __|        | |
    | |   _| |_ ___    | | ___   ___ | |
    | |  | | __/ _ \   | |/ _ \ / _ \| |
    | |  | | ||  __/   | | (_) | (_) | |
    |_|  |_|\__\___|   |_|\___/ \___/|_|
                                        
""")
        print('LESSON 5 CODES:\n')
        print('1. Generate Tuples with Numbers and Their Squares')
        print('2. Divisible Tuples from Integer Tuple List')
        print('3. Manage Days in Months')
        print('4. Manage Products and Prices')
        print('5. User Authentication System')
        print('6. Go back to the main menu\n')
        ch = input('Enter choice here: ')
        choice = int(ch)
        if choice in range(1, 6):
            switch_for_lesson5(choice)
        elif choice == 6:
            break
        else:
            print(Fore.RED + '\nError: Invalid input! Please enter a valid choice...' + Style.RESET_ALL)

def display_thank_you():
    clear_console()
    print(Fore.YELLOW + """
  ____             _     ____        _   
 / ___| _ __  _ __(_)___| __ ) _   _| |_ 
 \___ \| '_ \| '__| / __|  _ \| | | | __|
  ___) | |_) | |  | \__ \ |_) | |_| | |_ 
 |____/| .__/|_|  |_|___/____/ \__,_|\__|
       |_|                               
""")
    print('THANK YOU FOR USING THE PROGRAM!\n')
    print('We hope you found it helpful and enjoyable.')
    print('Have a great day!\n')


def main():
    intro()
    while True:
        display_main_menu()
        ch = input('Enter choice here: ')
        choice = ch.upper()

        if choice == 'A':
            display_lesson4_menu()
        elif choice == 'B':
            display_lesson5_menu()
        elif choice == 'E':
            clear_console()
            display_thank_you()
            break
        else:
            print(Fore.RED + '\nError: Invalid input! Please enter a valid option!' + Style.RESET_ALL)
            input('\nPress any key to continue...')

if __name__ == "__main__":
    main()
