import os # for clearing the console / screen
from Lesson4 import less4_code1, less4_code2, less4_code3, less4_code4, less4_code5, less4_code6
from Lesson5 import less5_code1, less5_code2, less5_code3, less5_code4, less5_code5

# ANSI color escape codes
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear_console()
    ascii_art = f"""
{Color.HEADER}░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝{Color.ENDC}
"""
    print(ascii_art)
    input(f'\n{Color.WARNING}Press any key to see the welcome message...{Color.ENDC}')
    clear_console()
    print(f'{Color.GREEN} ===============================================================')
    print(f'|               {Color.HEADER}WELCOME TO COMPILATION OF CODES!                {Color.GREEN}|')
    print(f'|                                                               |')
    print(f'|     This program is a compilation of all the codes in         |')
    print(f'|             {Color.BLUE}Lesson 4 {Color.GREEN}and {Color.BLUE}Lesson 5  {Color.GREEN}in the subject             |')
    print(f'|                                                               |')
    print(f'|                    {Color.BLUE}Integrative Programming                    {Color.GREEN}|')
    print(f' ==============================================================={Color.ENDC}')
    input(f'\n{Color.WARNING}Press any key to go to the main program...{Color.ENDC}')


def display_main_menu():
    clear_console()
    print(f'{Color.GREEN} ======================================')
    print(f'|              {Color.HEADER}Main Menu{Color.GREEN}               |')
    print(f' ======================================{Color.ENDC}')
    print(f'|     {Color.BLUE}Lesson 4     {Color.GREEN}|      {Color.BLUE}Lesson 5     {Color.GREEN}|')
    print(f'|       ( {Color.HEADER}A {Color.GREEN})      |       ( {Color.HEADER}B {Color.GREEN})       |')
    print(f'|--------------------------------------|')
    print(f'|                 {Color.WARNING}Exit                 {Color.GREEN}|')
    print(f'|                 ( {Color.FAIL}E {Color.GREEN})                |')
    print(f' ======================================{Color.ENDC}')

def switch_for_lesson4(choice):
    if choice == 1:
        clear_console()
        less4_code1.Program().main()  # call the first code in lesson 4 if user's choice is 1
    elif choice == 2:
        clear_console()
        less4_code2.Program().main()  # call the second code in lesson 4 if user's choice is 2
    elif choice == 3:
        clear_console()
        less4_code3.Program().main()  # call the third code in lesson 4 if user's choice is 3
    elif choice == 4:
        clear_console()
        less4_code4.Program().main()  # call the fourth code in lesson 4 if user's choice is 4
    elif choice == 5:
        clear_console()
        less4_code5.Program().main()  # call the fifth code in lesson 4 if user's choice is 5
    elif choice == 6:
        clear_console()
        less4_code6.Program().main()  # call the sixth code in lesson 4 if user's choice is 5
    else:
        print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid option!{Color.ENDC}')

def display_lesson4_menu():
    while True:
        clear_console()
        print(f' {Color.GREEN}=========================================================================={Color.ENDC}')
        print(f'|{Color.HEADER}                                LESSON 4 CODES                            {Color.GREEN}|')
        print(f' {Color.GREEN}=========================================================================={Color.ENDC}')
        print(f'| {Color.BLUE}1. List Manipulation and Slicing                                         {Color.GREEN}|')
        print(f'| {Color.BLUE}2. Adding, Finding Index, and Removing Items in the List                 {Color.GREEN}|')
        print(f'| {Color.BLUE}3. List Methods in Use: Append, Insert, Index, Count, Pop, and Remove    {Color.GREEN}|')
        print(f'| {Color.BLUE}4. Change Value, Add, Remove, Sort and Perform Operation in the List     {Color.GREEN}|')
        print(f'| {Color.BLUE}5. Factor List Generator: Create a List of Factors from User Input       {Color.GREEN}|')
        print(f'| {Color.BLUE}6. Removing Repeated Items in the List                                   {Color.GREEN}|')
        print(f'| {Color.BLUE}7. Go back to the main menu                                              {Color.GREEN}|')
        print(f' {Color.GREEN}=========================================================================={Color.ENDC}')
        ch = input('Enter choice here: ')
        choice = int(ch)
        if choice in range(1, 7):
            switch_for_lesson4(choice)
        elif choice == 7:
            break
        else:
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid choice...{Color.ENDC}')

def switch_for_lesson5(choice):
    if choice == 1:
        clear_console()
        less5_code1.Program().main()  # call the first code in lesson 5 if user's choice is 1
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
        print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid option!{Color.ENDC}')

def display_lesson5_menu():
    while True:
        clear_console()
        print(f' {Color.GREEN}======================================================{Color.ENDC}')
        print(f'|{Color.HEADER}                    LESSON 5 CODES                    {Color.GREEN}|')
        print(f' {Color.GREEN}======================================================{Color.ENDC}')
        print(f'| {Color.BLUE}1. Generate Tuples with Numbers and Their Squares.   {Color.GREEN}|')
        print(f'| {Color.BLUE}2. Divisible Tuples from Integer Tuple List.         {Color.GREEN}|')
        print(f'| {Color.BLUE}3. Manage Days in Months                             {Color.GREEN}|')
        print(f'| {Color.BLUE}4. Manage Products and Prices                        {Color.GREEN}|')
        print(f'| {Color.BLUE}5. User Authentication System                        {Color.GREEN}|')
        print(f'| {Color.BLUE}6. Go back to the main menu                          {Color.GREEN}|')
        print(f' {Color.GREEN}======================================================{Color.ENDC}')
        ch = input('Enter choice here: ')
        choice = int(ch)
        if choice in range(1, 6):
            switch_for_lesson5(choice)
        elif choice == 6:
            break
        else:
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid choice...{Color.ENDC}')

def display_thank_you():
    print(f' {Color.GREEN}======================================')
    print(f'|                                      |')
    print(f'|               {Color.WARNING}THANK YOU              {Color.GREEN}|')
    print(f'|         {Color.WARNING}FOR USING THE PROGRAM!       {Color.GREEN}|')
    print(f'|                                      |')
    print(f' {Color.GREEN}======================================{Color.ENDC}')

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
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid option!{Color.ENDC}')
            input('\nPress any key to continue...')

if __name__ == "__main__":
    main()
