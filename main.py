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

        
member_id = input("Member ID: ")
password = input("Password: ")

member_details = login(member_id, password)
