# IMPORTS
from helper import *
from menu_functions import *

def menu(library_name, member_details, menu_options):

    # Initialise variable
    valid_choice = False

    while valid_choice == False:

        print(f"Welcome, {member_details["name"]}, to {library_name}.")
        print() # Formatting

        for index, option in enumerate(menu_options, start=1):
            print(f"{index} - {option}")
        print() # Formatting

        choice = input("What would you like to do today? ")

        match choice:
            case '1':
                return borrow_book()
            case '2':
                return renew_book()
            case '3':
                return return_book()
            case '4':
                return membership_details()
            case _:
                print("Please choose a valid selection (1 - 4)")
                input("Press ENTER to continue.")
                clear_screen()
