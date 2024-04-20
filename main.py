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
    print(f"    {Color.GREEN}__________________________________   ____________________________________")
    print(f".-/                                  \\ /                                    |\\-.")
    print(f"||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||   {Color.HEADER}WELCOME TO COMPILATION OF CODES!  {Color.GREEN}|          MEMBERS OF GROUP 3         ||||")
    print(f"||  ---------------------------------  |  ---------------------------------  ||||")
    print(f"||                                     |                                     ||||")
    print(f"||                                     |            {Color.BLUE}Aloveros, Baron          {Color.GREEN}||||")
    print(f"||    This program is a compilation    |          {Color.BLUE}Estanislao, Ran-jel        {Color.GREEN}||||")
    print(f"||     of all the codes in Lesson 4    |         {Color.BLUE}Marial, Erice Michael       {Color.GREEN}||||")
    print(f"||     and Lesson 5 in the subject.    |          {Color.BLUE}Sinday, Ellen Grace        {Color.GREEN}||||")
    print(f"||                                     |          {Color.BLUE}Solano, Cedric Mark        {Color.GREEN}||||")
    print(f"||                                     |          {Color.BLUE}Vargas, Ashley John        {Color.GREEN}||||")
    print(f"||                                     |                                     ||||")
    print(f"||                                     |                                     ||||")
    print(f"||       {Color.BLUE}Integrative Programming       {Color.GREEN}|                        (Enter) -->  ||||")
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
            print(f"    {Color.GREEN}____________________________________   ____________________________________")
            print(f".-/|                                    \\ /                                    |\\-.")
            print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
            print(f"||||            {Color.HEADER}LESSON 4 CODES           {Color.GREEN}|            {Color.HEADER}LESSON 4 CODES           {Color.GREEN}||||")
            print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
            print(f"||||                                     |                                     {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}1. List Manipulation and Slicing  {Color.GREEN}|   {Color.BLUE}5. Factor List Generator:         {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}2. Adding, Finding Index, and     {Color.GREEN}|      {Color.BLUE}Create a List of Factors from  {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}Removing Items in the List     {Color.GREEN}|      {Color.BLUE}User Input                     {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}3. List Methods in Use: Append,   {Color.GREEN}|   {Color.BLUE}6. Removing Repeated Items in     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}Insert, Index, Count, Pop,     {Color.GREEN}|      {Color.BLUE}the List                       {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}and Remove                     {Color.GREEN}|   {Color.BLUE}7. Go back to the main menu       {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}4. Change Value, Add, Remove,     {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}Sort and Perform Operation in  {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}the List                       {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||____________________________________ | ____________________________________{Color.GREEN}||||")
            print(f"||/=====================================\\|/=====================================\\{Color.GREEN}||")
            print(f"`--------------------------------------~___~-------------------------------------'")
            ch = input(f'{Color.WARNING}Enter choice here: {Color.ENDC}')
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
            print(f"    {Color.GREEN}____________________________________   ____________________________________")
            print(f".-/|                                    \\ /                                    |\\-.")
            print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
            print(f"||||            {Color.HEADER}LESSON 5 CODES           {Color.GREEN}|            {Color.HEADER}LESSON 5 CODES           {Color.GREEN}||||")
            print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
            print(f"||||                                     |                                     {Color.GREEN}||||")
            print(f"||||                                     |                                     {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}1. Generate Tuples with Numbers   {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}and Their Squares.             {Color.GREEN}|   {Color.BLUE}4. Manage Products and Price      {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}2. Divisible Tuples from Integer  {Color.GREEN}|   {Color.BLUE}5. User Authentication System     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}Tuple List.                    {Color.GREEN}|   {Color.BLUE}6. Go back to the main menu       {Color.GREEN}||||")
            print(f"||||   {Color.BLUE}3. Manage Days in Months          {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||      {Color.BLUE}and Remove                     {Color.GREEN}|                                     {Color.GREEN}||||")
            print(f"||||                                     |                                     {Color.GREEN}||||")
            print(f"||||                                     |                                     {Color.GREEN}||||")
            print(f"||||____________________________________ | ____________________________________{Color.GREEN}||||")
            print(f"||/=====================================\\|/=====================================\\{Color.GREEN}||")
            print(f"`--------------------------------------~___~-------------------------------------'")
            ch = input(f'{Color.WARNING}Enter choice here: {Color.ENDC}')
            choice = int(ch)
            if choice in range(1, 6):
                switch_for_lesson5(choice)
            elif choice == 6:
                break
            else:
                print(f'\n{Color.FAIL}Error: Invalid input! Please enter a valid choice...{Color.ENDC}')
        except ValueError:
            print(f'\n{Color.FAIL}Error: Invalid input! Please enter an integer.{Color.ENDC}')
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
    print(f"    {Color.GREEN}____________________________________   ____________________________________")
    print(f".-/|                                    \\ /                                    |\\-.")
    print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
    print(f"||||  {Color.HEADER}---------------------------------  |          {Color.HEADER}MEMBERS OF GROUP 3         {Color.GREEN}||||")
    print(f"||||  {Color.HEADER}---------------------------------  |  ---------------------------------  {Color.GREEN}||||")
    print(f"||||                                     |                                     {Color.GREEN}||||")
    print(f"||||                                     |                                     {Color.GREEN}||||")
    print(f"||||    {Color.BLUE}-----------------------------    {Color.GREEN}|            {Color.BLUE}Aloveros, Baron          {Color.GREEN}||||")
    print(f"||||     {Color.BLUE}----------------------------    {Color.GREEN}|          {Color.BLUE}Estanislao, Ran-jel        {Color.GREEN}||||")
    print(f"||||     {Color.BLUE}----------------------------    {Color.GREEN}|         {Color.BLUE}Marial, Erice Michael       {Color.GREEN}||||")
    print(f"||||                                     |          {Color.BLUE}Sinday, Ellen Grace        {Color.GREEN}||||")
    print(f"||||                                     |          {Color.BLUE}Solano, Cedric Mark        {Color.GREEN}||||")
    print(f"||||                                     |          {Color.BLUE}Vargas, Ashley John        {Color.GREEN}||||")
    print(f"||||                                     |                                     {Color.GREEN}||||")
    print(f"||||  <-- {Color.WARNING}(Enter) ----------------       {Color.GREEN}|                                     {Color.GREEN}||||")
    print(f"||||____________________________________ | ____________________________________{Color.GREEN}||||")
    print(f"||/=====================================\\|/=====================================\\{Color.GREEN}||")
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