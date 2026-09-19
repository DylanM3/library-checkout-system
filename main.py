# PYTHON LIBRARY SYSTEM

# IMPORTS AND INITS
from login import login
from menu import menu
from helper import clear_screen
import json

menu_options = [
    "Borrow a Book",
    "Renew a Book",
    "Return a Book",
    "View Account Details",
    "Exit"
]

# LOAD DATABASE.JSON INTO PYTHON
with open("database.json") as db:
    data = json.load(db)

# DECOMPILE THE NESTED JSON INTO MULTIPLE LISTS
library_name = data["library_name"]
books = data.pop("books", {})
members = data.pop("members", {})
loans = data.pop("loans", {})

# REPEAT LOGIN UNTIL VALID DETAILS ARE PROVIDED
while True:

    # HANDLE USER LOGIN - STORE USER INFO
    member_id = input("Member ID: ")
    password = input("Password: ")
    member_details = login(member_id, password, members)

    clear_screen()

    if member_details:
        break

# PROGRAM LOOP BEGINS
menu(library_name, member_details, menu_options, books, loans)