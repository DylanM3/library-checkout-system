# PYTHON LIBRARY SYSTEM

# IMPORTS AND INITS
import json

# LOAD DATABASE.JSON INTO PYTHON
with open("database.json") as db:
    global data
    data = json.load(db)

print(f"Welcome to {data["library_name"]}!")

# SIGN IN
# Loops over every member with O(n) complexity until ID matched or it returns failure
def login(user_member_id):
    for member in data["members"]:
        current_member_id = (member["member_id"])
        if user_member_id == current_member_id:
            return True

    return False
        
user_member_id = input("Member ID: ")

login_result = login(user_member_id)
if login_result == True:
    print("Success.")
else:
    print("ID not recognised. Please try again.")