class SearchContact:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def search_contact(self, name):
        if name in self.contacts:
            return f"Контакт {name}: {self.contacts[name]}"
        else:
            return f"Контакт {name} не знайдено."

    def edit_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return f"Контакт {name} відредаговано."
        else:
            return f"Контакт {name} не знайдено."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Контакт {name} видалено."
        else:
            return f"Контакт {name} не знайдено."
