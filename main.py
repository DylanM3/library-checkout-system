# PYTHON LIBRARY SYSTEM

# IMPORTS AND INITS
from login import login
from menu import menu
from helper import *
import json

login_success = False
menu_options = ["Borrow a book", "Renew a Book", "Return a Book", "View Account Details"]

# LOAD DATABASE.JSON INTO PYTHON
with open("database.json") as db:
    data = json.load(db)

# DECOMPILE THE NESTED JSON INTO MULTIPLE DICTS
library_name = data["library_name"]
books_dict = data.pop("books", {})
members_dict = data.pop("members", {})
loans_dict = data.pop("loans", {})

# REPEAT LOGIN UNTIL SUPPLIED WITH VALID DETAILS
while login_success == False:

    # HANDLE USER LOGIN - STORE USER INFO
    member_id = input("Member ID: ")
    password = input("Password: ")
    member_details = login(member_id, password, members_dict)

    clear_screen()

    if member_details:
        # PROGRAM LOOP HERE
        menu(library_name, member_details, menu_options)