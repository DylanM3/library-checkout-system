# IMPORTS
from helper import *

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
                #return borrow_book()
                pass
            case '2':
                #return renew_book()
                pass
            case '3':
                #return return_book()
                pass
            case '4':
                #return membership_details()
                pass
            case _:
                print("Please choose a valid selection (1 - 4)")
                input("Press ENTER to continue.")
                clear_screen()
