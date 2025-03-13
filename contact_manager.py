# Contact manager application
# add_contact for adding a contact
# view_contacts for display the contact
# search_contact for fetch a specific contact by name
# update_contact for update a contact details by name
# delete_contact for delete a contact from list
contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    for contact in contacts:
        if contact[0] == name:
            print("Contact already exists!")
            return
    
    contacts.append((name, phone, email))
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found!\n")
        return
    
    print("List of Contacts:")
    for i, (name, phone, email) in enumerate(contacts, 1):
        print(f"{i}. {name} - {phone} - {email}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}\n")
            return
    print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ")
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            new_phone = input("Enter new phone number: ")
            contacts[i] = (contact[0], new_phone, contact[2])  
            print("Contact updated successfully")
            return
    print("Contact not found!")


def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact[0].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

while True:
    print("\nWelcome to Contact Manager")
    print("1. Add Contact\n2. View Contacts\n3. Search Contact")
    print("4. Update Contact\n5. Delete Contact\n6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Manager. Goodbye!\n")
        break
    else:
        print("Invalid choice! Please enter a number between 1-6.\n")

