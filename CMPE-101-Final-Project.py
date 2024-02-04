'''************************************************************************
                      CMPE 102 Programming Logic and Design
                                 GROUP FINAL Project

   Programmed By:
        Joshua Mistal
        Ralph Daniel Jimenez
        Miel Gagolinan
        Jo Mari Raphael Mangahas
        Mark Brin
   Course and Section: BSCpE 1-3
   Instructor: Prof. Engr. Julius S. Cansino
    Class Schedule: Saturday 2:00 PM - 8:00PM
   Date Performed: February 3, 2024
   Date Submitted: Februar 5, 2024

Address Book Functionalities:
(1) Add Contact - Developed by Joshua Mistal
(2) Edit Contact - Developed by Mark Brin
(3) Delete Contact - Developed by Miel Gagolinan
(4) View Contacts - Developed by Ralph Daniel
(5) Search Address Book - Developed by Jo Mari Raphael Mangahas
(Utility) Display Menu, Choose, Input Int, Display Contacts - Developed by Joshua Mistal

************************************************************************'''

features = [
    "Add Contact",
    "Edit Contact",
    "Delete Contact",
    "View Contacts",
    "Search Address Book",
    "Exit"
]

def display_menu():
    '''Displays the header border and menu for the address book features'''
    # Set the width for the header
    width = 10

    # Print the header with the specified width
    print("-" * width, "Address Book", "-" * width)

    # Display all the available options
    for i, option in enumerate(features, start=1):
        print(f"{i}. {option}")

    # Print an empty line space for better readability
    print("")

def choose() -> int:
    '''Allows the user to choose from 1 to 6 (the number to interact with the address book).'''
    option = 0

    # Keep running until the user provides a valid option
    while not option or not (0 < option <= len(features)):
        option = input_int("Choose an option: ")
        if not (0 < option <= len(features)):
            print("Invalid Option..")

    return option

def display_contacts(contacts, start = 0, end = 0):
    '''Display a list of contacts information with their firstname and contact number' at a specified length'''
    if not end:
        end = len(contacts)

    # Find the max name legnth to align the name values and contacts
    max_name_length = max(len(f"{contact['first_name']} {contact['last_name']}") for contact in contacts)

    # Print Header
    print(f"\n[##] {"Name".center(max_name_length,"-")} | ----Number----")

    # Iterate and print the contact information
    for i in range(start, end):
        contact = contacts[i]
        name = f"{contact['first_name']} {contact['last_name']}"
        number = contact["contact_no"]
        print(f"[{(i+1):>2}] {name:<{max_name_length}} | {number}")

def input_int(message = "Enter an integer: ") -> int:
    '''Data validation. Typecasts input into integer and checks for edge cases when inputting numbers from user.'''
    while True:
        try:
            num_input = int(input(message).strip())
            return num_input
        except ValueError:
            print('Invalid Input.\n')

def add_contact(contacts):
    '''Prompt the user for the first name, last name, address, and contact number.'''
    if len(contacts) > 99:
        print("Limit for contacts in your address book has been reached!\n")
        return
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    contact_no = input_int("Enter your contact number: ")

    # Assign these entries to a dict of entries
    entries = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "contact_no": contact_no
    }

    # Add the user entry into the contacts collection
    contacts.append(entries)

    # Return the contacts with the newly added person
    return contacts

def edit_contact(contacts):
    """Prompt the user for the entry number he wants to edit."""

    # Display the contactsB
    display_contacts(contacts)

    entry_edit = input_int("Enter the entry number to be edited: ")

    while True:
        try:
            entry_n = contacts[entry_edit - 1]
            # Displays the current details of the specified entry.
            display_contacts([entry_n])

            # Prompts the user which part of entry details to be edited.
            print("\n--- Select what to edit to the entry ---\n",
                "1. Edit first name.\n",
                "2. Edit last name.\n",
                "3. Edit address.\n",
                "4. Edit contact number.\n",
                "5. Exit edit.\n")

            edit_option = input_int("Enter option number: ")

            # Prompts the user to edit entries depending on specified detail.
            if edit_option == 1:
                updated_entry = {"first_name": input("Enter new first name: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:", entry_n)
            elif edit_option == 2:
                updated_entry = {"last_name": input("Enter new last name: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:", entry_n)
            elif edit_option == 3:
                updated_entry = {"address": input("Enter new address: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:", entry_n)
            elif edit_option == 4: # Edit Contact
                updated_entry = {"contact_no": input_int("Enter new contact number: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:", entry_n)
            elif edit_option == 5:# Exit
                print("Exiting edit.")
            else: # For edge cases
                print("Invalid option!")

            break

        except IndexError: # no key excists
            print("No entry found!")

def delete_contact(contacts):
    """Prompt the user to enter the entry number to be deleted.b.
    After deleting a record, all succeeding entries will move forward."""

    # Don't run when no contacts exists
    if not contacts:
        print("No existing entries")
        return

    # Display the contacts
    display_contacts(contacts)

    print(contacts)

    while True:
        # Prompt the user to input an contact entry to choose
        erase_index = input_int("Enter entry number you want to delete: ")

        # Check if index to erase is within contacts range
        if not (0 < erase_index <= len(contacts)):
            print("Input number out of range")
            continue

        # Confirm deletion
        confirm = input("Are you sure you want to delete this?(y/n): ").strip().lower()
        if confirm != 'y':
            print("Canceling deletion...\n")
            break

        # Delete the contacts from the list
        deleted = contacts.pop((erase_index)-1)
        print(f"Successfully Deleted {deleted['first_name']} {deleted['last_name']}...\n")

        # Ask the user for another deletion
        repeat = input("you want to delete another entry?(y/n): ").strip().lower()
        if repeat == "n":
            print("Exiting...\n")
            break

def view_contacts(contacts):
    '''Display all the entries.'''
    page_number = 1

    while True:
        # Display contacts at specific page
        page_size = 10
        start_index = (page_number - 1) * page_size
        end_index = min(start_index + page_size, len(contacts))

        # Display the contacts
        display_contacts(contacts, start = start_index, end = end_index)

        # Display the rest of the empty filled contacts
        for i in range(end_index, start_index + page_size):
            print(f"[{i+1}] ...")


        print("\n<<< (P)revious | Page", page_number, "| (N)ext>>>")
        print("[ Press ENTER to return to exit ]")

        user_input = input().strip().lower()

        if user_input == "p" and page_number > 1:
            page_number -= 1
        elif user_input == "n" and page_number * 10 < len(contacts):
            page_number += 1
        elif user_input == "":
            break

        else:
            print("Invalid input. Please enter (P)revious, (N)ext, or press ENTER to return to main.")

def search_contacts(contacts):
    '''Prompt  the  user  to  search  the  address  book
    (a)  by  first  name,
    (b)  by  last  name,
    (c)  by address or
    (d) by contact number.
    Display all the entries that matched the query. Else, notify the user that the entry doesn\'t exist
    '''
    if not contacts:
        print("Address book is empty. No contacts to search.")
        return

    while True:
        found_contacts = []
        print("\nSearch Options\nA) First Name\nB) Last Name\nC) Address\nD) Contact Number")
        option_prompt = input("Enter option: ").strip().upper()

        search_query = input("Enter search query: ").strip().title()
        print(search_query)
        # Search through contacts
        for contact in contacts:
            if option_prompt == 'A' and search_query in contact['first_name']:
                found_contacts.append(contact)
            elif option_prompt == 'B' and search_query in contact['last_name']:
                found_contacts.append(contact)
            elif option_prompt == 'C' and search_query in contact["address"]:
                found_contacts.append(contact)
            elif option_prompt == 'D'and search_query in contact['contact_no']:
                found_contacts.append(contact)
        print("")
        if not found_contacts:
            print("No Entries Found!\n")
        else:
            display_contacts(found_contacts)

        again = input("Do you want to search other entries? (Yes/No) ").lower()
        if again != 'yes':
            break


def main():
    '''Main Program'''

    # Initialize the address book object
    address_book = []

    while True:
        # Display the Menu
        display_menu()

        # Choose an Option
        option = choose()

        # Perform actions to address_book based on the user's choice
        match option:
            case 1:
                add_contact(address_book)
            case 2:
                edit_contact(address_book)
            case 3:
                delete_contact(address_book)
            case 4:
                view_contacts(address_book)
            case 5:
                search_contacts(address_book)
            case 6:
                # Exit the program
                print("Exiting...")
                break

if __name__ == "__main__":
    main()