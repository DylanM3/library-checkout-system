def menu(library_name, member_details, menu_options):

    print(member_details)

    print(f"Welcome, {member_details["name"]} to {library_name}.")
    print() # Formatting

    for index, option in enumerate(menu_options):
        print(f"{index} - {option}")