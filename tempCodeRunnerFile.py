def edit_contact(contacts):
    """Prompt the user for the entry number he wants to edit."""

    # Don't run when no contacts exists
    if not contacts:
        print("No existing entries")
        return

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
                print("Updated entry details:")
                display_contacts([entry_n])
            elif edit_option == 2:
                updated_entry = {"last_name": input("Enter new last name: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:")
                display_contacts([entry_n])
            elif edit_option == 3:
                updated_entry = {"address": input("Enter new address: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:")
                display_contacts([entry_n])
            elif edit_option == 4: # Edit Contact
                updated_entry = {"contact_no": input_int("Enter new contact number: ")}
                entry_n.update(updated_entry)
                print("Updated entry details:")
                display_contacts([entry_n])
            elif edit_option == 5:# Exit
                print("Exiting edit.")
            else: # For edge cases
                print("Invalid option!")

            break

        except IndexError: # no key excists
            print("No entry found!")

def delete_contact(contacts):
