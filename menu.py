from helper import clear_screen
from menu_functions import (
    borrow_book,
    renew_book,
    return_book,
    membership_details
)

def menu(library_name, member_details, menu_options, books, loans):

    while True:

        clear_screen()

        print(f"Welcome, {member_details['name']}, to {library_name}.")
        print() # Formatting

        for index, option in enumerate(menu_options, start=1):
            print(f"{index} - {option}")

        print() # Formatting

        choice = input("What would you like to do today? ")

        match choice:

            case "1":
                borrow_book(member_details, books, loans)
            case "2":
                renew_book(member_details, books, loans)
            case "3":
                return_book(member_details, books, loans)
            case "4":
                membership_details(member_details)
            case '5':
                clear_screen()
                print(f"Goodbye, {member_details["name"]}")
                print(f"Thank you for visiting {library_name}.")
                return
            case _:
                print("Please choose a valid selection (1 - 4)")
                input("Press ENTER to continue.")