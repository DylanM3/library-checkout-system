from helper import *

def borrow_book(membership_details):
    pass

def renew_book(membership_details):
    pass

def return_book(membership_details):
    pass


def membership_details(member_details):

    clear_screen()

    password = member_details["password"]
    truncated_password = password[:4] + "*" * max(0, len(password) - 4)

    print(f"Name: {member_details['name']}")
    print(f"Password: {truncated_password}")
    print(f"Joined: {member_details['membership_date']}")
    print(f"Membership ID: {member_details['member_id']}")

    print()
    input("Press ENTER to return to the menu.")