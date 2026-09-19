# PYTHON LIBRARY SYSTEM

# IMPORTS AND INITS
import json

# LOAD DATABASE.JSON INTO PYTHON
with open("database.json") as db:
    global data
    data = json.load(db)

# DECOMPILE THE NESTED JSON INTO MULTIPLE DICTS
library_name = data["library_name"]
books_dict = data.pop("books", {})
members_dict = data.pop("members", {})
loans_dict = data.pop("loans", {})

# SIGN IN FUNCTION
# Loops over every member with O(n) complexity until ID matched or it returns failure
def login(member_id, password):

    # Initialise variable
    member_details = None

    for member in members_dict:

        # Grab the correct login info from the dictionarys
        system_member_id = member["member_id"]
        system_password = member["password"]

        # Compare the information to the correct information
        if member_id == system_member_id:
            member_id_approved = True
        else:
            member_id_approved = False

        if password == system_password:
            password_approved = True
        else:
            password_approved = False

        # Check if ALL the information is correct
        if member_id_approved and password_approved:
            member_details = member

    # Check if a member was found
    if member_details:
        print(f"Welcome, {member_details["name"]}.")
    else:
        print("Login Failed.\nPlease re-run the program and try again.")

        
member_id = input("Member ID: ")
password = input("Password: ")

member_details = login(member_id, password)
