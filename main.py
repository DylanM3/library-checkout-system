# PYTHON LIBRARY SYSTEM

# IMPORTS AND INITS
import json
current_user = []

# LOAD DATABASE.JSON INTO PYTHON
with open("database.json") as db:
    global data
    data = json.load(db)

# DECOMPILE THE NESTED JSON INTO MULTIPLE DICTS
library_name = data["library_name"]
books_dict = data.pop("books", {})
members_dict = data.pop("members", {})
loans_dict = data.pop("loans", {})

def login()














# # SIGN IN FUNCTION
# # Loops over every member with O(n) complexity until ID matched or it returns failure
# def login(given_member_id):
#     for member in members_dict:
#         current_member_id = member["member_id"]
#         if given_member_id == current_member_id:
#             return True
#     return False # Checked all members, no ID matched

# given_member_id = input("Member ID Number: ")
# login_results = login(given_member_id)

# if login_results == True:
#     index_number = int(members_dict[1:]) - 1
#     current_user.append(members_dict[index_number])
#     print(current_user)
# else:
#     print("ID not recognised.\nPlease try again.")