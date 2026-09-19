# SIGN IN FUNCTION
# Loops over every member with O(n) complexity until ID matched or it returns failure
def login(member_id, password, members_dict):

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
        return member_details
    else:
        print("Login Failed.\nPlease re-run the program and try again.")