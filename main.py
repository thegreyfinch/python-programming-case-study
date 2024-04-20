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
    {Color.HEADER}
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
    {Color.ENDC}
    """
    print(ascii_art)
    input(f'\n{Color.WARNING}Press Enter to see the welcome message...{Color.ENDC}')
    clear_console()
    print(f"    __________________________________   ____________________________________")
    print(f".-/                                  \\ /                                    |\\-.")
    print(f"||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||   WELCOME TO COMPILATION OF CODES!  |          MEMBERS OF GROUP 3         ||||")
    print(f"||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||                                     |                                     ||||")
    print(f"||                                     |            Aloveros, Baron          ||||")
    print(f"||    This program is a compilation    |          Estanislao, Ran-jel        ||||")
    print(f"||     of all the codes in Lesson 4    |         Marial, Erice Michael       ||||")
    print(f"||     and Lesson 5 in the subject.    |          Sinday, Ellen Grace        ||||")
    print(f"||                                     |          Solano, Cedric Mark        ||||")
    print(f"||                                     |          Vargas, Ashley John        ||||")
    print(f"||                                     |                                     ||||")
    print(f"||                                     |                                     ||||")
    print(f"||       Integrative Programming       |                        (Enter) -->  ||||")
    print(f"||                                     | ____________________________________||||")
    print(f"||_____________________________________|/=====================================\\||")
    print(f"`------------------------------------~___~-------------------------------------'")
    input(f'\n{Color.WARNING}Press Enter to go to the main program...{Color.ENDC}')


def display_main_menu():
    clear_console()
    print(f'{Color.GREEN} ======================================')
    print(f'|              {Color.HEADER}Main Menu{Color.GREEN}               |')
    print(f' ======================================')
    print(f'|{Color.ENDC}     {Color.BLUE}Lesson 4     {Color.GREEN}|      {Color.BLUE}Lesson 5     {Color.GREEN}|')
    print(f'|       ( {Color.HEADER}A {Color.GREEN})      |       ( {Color.HEADER}B {Color.GREEN})       |')
    print(f'|--------------------------------------|')
    print(f'|            {Color.BLUE}Display Members{Color.GREEN}           |')
    print(f'|                 ( {Color.HEADER}C {Color.GREEN})                |')
    print(f'|--------------------------------------|')
    print(f'|                 {Color.WARNING}Exit                 {Color.GREEN}|')
    print(f'|                 ( {Color.FAIL}E {Color.GREEN})                |')
    print(f' ======================================{Color.ENDC}')


def display_lesson4_menu():
    while True:
        try:
            clear_console()
            print(f"    ____________________________________   ____________________________________")
            print(f".-/|                                    \\ /                                    |\\-.")
            print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
            print(f"||||            LESSON 4 CODES           |            LESSON 4 CODES           ||||")
            print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
            print(f"||||                                     |                                     ||||")
            print(f"||||   1. List Manipulation and Slicing  |   5. Factor List Generator:         ||||")
            print(f"||||   2. Adding, Finding Index, and     |      Create a List of Factors from  ||||")
            print(f"||||      Removing Items in the List     |      User Input                     ||||")
            print(f"||||   3. List Methods in Use: Append,   |   6. Removing Repeated Items in     ||||")
            print(f"||||      Insert, Index, Count, Pop,     |      the List                       ||||")
            print(f"||||      and Remove                     |   7. Go back to the main menu       ||||")
            print(f"||||   4. Change Value, Add, Remove,     |                                     ||||")
            print(f"||||      Sort and Perform Operation in  |                                     ||||")
            print(f"||||      the List                       |                                     ||||")
            print(f"||||____________________________________ | ____________________________________||||")
            print(f"||/=====================================\\|/=====================================\\||")
            print(f"`--------------------------------------~___~-------------------------------------'")
            ch = input('Enter choice here: ')
            choice = int(ch)
            if choice in range(1, 7):
                switch_for_lesson4(choice)
            elif choice == 7:
                break
            else:
                print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid choice...{Color.ENDC}')
        except ValueError:
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter an integer.{Color.ENDC}')
            input('Press Enter to input again...')

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

def display_lesson5_menu():
    while True:
        try:
            clear_console()
            print(f"    ____________________________________   ____________________________________")
            print(f".-/|                                    \\ /                                    |\\-.")
            print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
            print(f"||||            LESSON 5 CODES           |            LESSON 5 CODES           ||||")
            print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
            print(f"||||                                     |                                     ||||")
            print(f"||||                                     |                                     ||||")
            print(f"||||   1. Generate Tuples with Numbers   |                                     ||||")
            print(f"||||      and Their Squares.             |   4. Manage Products and Price      ||||")
            print(f"||||   2. Divisible Tuples from Integer  |   5. User Authentication System     ||||")
            print(f"||||      Tuple List.                    |   6. Go back to the main menu       ||||")
            print(f"||||   3. Manage Days in Months          |                                     ||||")
            print(f"||||      and Remove                     |                                     ||||")
            print(f"||||                                     |                                     ||||")
            print(f"||||                                     |                                     ||||")
            print(f"||||____________________________________ | ____________________________________||||")
            print(f"||/=====================================\\|/=====================================\\||")
            print(f"`--------------------------------------~___~-------------------------------------''")
            ch = input('Enter choice here: ')
            choice = int(ch)
            if choice in range(1, 6):
                switch_for_lesson5(choice)
            elif choice == 6:
                break
            else:
                print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid choice...{Color.ENDC}')
        except ValueError:
            print('\nError: Invalid input! Please enter an integer...')
            input('Press Enter to input again...')

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

def display_members():
    clear_console()
    print(f"    ____________________________________   ____________________________________")
    print(f".-/|                                    \\ /                                    |\\-.")
    print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||||  ---------------------------------  |          MEMBERS OF GROUP 3         ||||")
    print(f"||||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||||                                     |                                     ||||")
    print(f"||||                                     |                                     ||||")
    print(f"||||    -----------------------------    |            Aloveros, Baron          ||||")
    print(f"||||     ----------------------------    |          Estanislao, Ran-jel        ||||")
    print(f"||||     ----------------------------    |         Marial, Erice Michael       ||||")
    print(f"||||                                     |          Sinday, Ellen Grace        ||||")
    print(f"||||                                     |          Solano, Cedric Mark        ||||")
    print(f"||||                                     |          Vargas, Ashley John        ||||")
    print(f"||||                                     |                                     ||||")
    print(f"||||  <-- (Enter) ----------------       |                                     ||||")
    print(f"||||____________________________________ | ____________________________________||||")
    print(f"||/=====================================\\|/=====================================\\||")
    print(f"`--------------------------------------~___~-------------------------------------'")
    input(f'\n{Color.WARNING}Press Enter to continue...{Color.ENDC}')


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
        elif choice == 'C':
            display_members()
        elif choice == 'E':
            clear_console()
            display_thank_you()
            break
        else:
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid option!{Color.ENDC}')
            input('\nPress Enter to continue...')

if __name__ == "__main__":
    main()
