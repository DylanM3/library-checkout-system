# SIGN IN FUNCTION
# Loops over every member with O(n) complexity until ID matched or it returns failure
def login(member_id, password, members):

    for member in members:

        if member["member_id"] == member_id and member["password"] == password:
            return member

    print("Login failed - please try again.")
    input("Press ENTER to continue.")

    return False
