class Phonebook:

    def __init__(self):
        self.contacts = {}

    def save_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def display_contacts(self):
        output = ""
        for name, phone_number in self.contacts.items():
            output += f"{name}: {phone_number}\n"
        return output

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def search_contact(self, query):
        return self.contacts.get(query)

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
        else:
            print(f"Contact '{name}' not found.")