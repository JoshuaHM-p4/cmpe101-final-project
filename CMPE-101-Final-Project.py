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
   Date Performed: January
   Date Submitted: January, 2024

NOTE TO PROGRAMMERS:
1. Consider using a class to encapsulate the address book functionality. ✔
    This can help with organization and make it easier to manage the state of the address book.

2.  Add comments to your code to explain the purpose of functions and any complex logic.
3.  Validate user inputs to handle potential errors (e.g., non-integer inputs, invalid options).
4. Use meaningful variable and function names to improve code readability.
5. Consider adding error handling to handle unexpected issues gracefully.

************************************************************************'''

FEATURES = [
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
    print("-"*width, "Address Book", "-"*width)

    # Display all the available options
    for i, option in enumerate(FEATURES, start=1):
        print(f"{i}. {option}")

    # Print an empty line space for better readability
    print("")

def choose() -> int:
    '''Allows the user to choose from 1 to 6 (the number to interact with the address book).'''
    option = 0

    # Keep running until the user provides a valid option
    while not option or not (0 < option <= len(FEATURES)):
        option = int(input("Choose an option: "))
        if not (0 < option <= len(FEATURES)):
            print("Invalid Option..")

    return option

class AddressBook:
    """
    Address Book Object
    With Functionalities:
        (1) Add Contact - Developed by Joshua Mistal
        (2) Edit Contact - Developed by Mark Brin
        (3) Delete Contact - Developed by Miel Gagolinan
        (4) View Contacts - Developed by Ralph Daniel
        (5) Search Address Book - Developed by Jo Mari Raphael Mangahas
    """

    def __init__(self):
        self.contacts = []

    def add_contact(self):
        '''Prompt the user for the first name, last name, address, and contact number.'''
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        address = input("Enter your addres: ")
        contact_no = int(input("Enter your contact number: "))

        # Assign these entries to a dict of entries
        entries = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "contact_no": contact_no
        }

        # Add the user entry into the contacts collection
        self.contacts.append(entries)

        # Return the contacts with the newly added newly added person
        return self.contacts


    def edit_contact(self):
        """Prompt the user for the entry number he wants to edit."""
        pass


    def delete_contact(self):
        """Prompt the user to enter the entry number to be deleted.b.
        After deleting a record, all succeeding entries will move forward."""
        pass

    def view_contacts(self):
        '''Display all the entries.'''
        pass

    def search_contacts(self):
        '''Prompt  the  user  to  search  the  address  book
        (a)  by  first  name,
        (b)  by  last  name,
        (c)  by address or
        (d) by contact number.
        Display all the entries that matched the query. Else, notify the user that the entry doesn\'t exist
        '''
        pass


def main():
    '''Main Program'''

    # Initialize the address book object
    address_book = AddressBook()

    while True::
        # Display the Menu
        display_menu()

        # Choose an Option
        option = choose()

        # Perform actions to address_book based on the user's choice
        match option:
            case 1:
                address_book.add_contact()
            case 2:
                address_book.edit_contact()
            case 3:
                address_book.delete_contact()
            case 4:
                address_book.view_contacts()
            case 5:
                address_book.search_contacts()
            case 6:
                # Exit the program
                break

if __name__ == "__main__":
    main()


