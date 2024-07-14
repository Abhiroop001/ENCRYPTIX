class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone_number]
        if not results:
            print("No matching contacts found!")
        else:
            print("Search Results:")
            for i, contact in enumerate(results, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{name}' updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print("Contact not found!")

def main():
    contact_manager = ContactManager()

    while True:
        print("\n WELCOME TO THE CONTACT MANAGEMENT PROGRAM \n")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_manager.view_contact_list()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number (optional): ")
            new_email = input("Enter new email (optional): ")
            new_address = input("Enter new address (optional): ")
            contact_manager.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()