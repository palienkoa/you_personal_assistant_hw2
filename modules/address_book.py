class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        """Додати контакт у книгу контактів."""
        self.contacts[name] = {"phone": phone}

    def search_contact(self, name):
        """Пошук контакту за ім'ям."""
        if name in self.contacts:
            return f"Контакт {name}: {self.contacts[name]['phone']}"
        else:
            return f"Контакт {name} не знайдено."

    def edit_contact(self, name, new_phone):
        """Редагування контакту за ім'ям."""
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone
            return f"Контакт {name} відредаговано."
        else:
            return f"Контакт {name} не знайдено."

    def delete_contact(self, name):
        """Видалення контакту за ім'ям."""
        if name in self.contacts:
            del self.contacts[name]
            return f"Контакт {name} видалено."
        else:
            return f"Контакт {name} не знайдено."

    def search_contacts(self, search_text):
        """Пошук контактів за текстовим запитом."""
        found_contacts = []
        for name, data in self.contacts.items():
            if search_text.lower() in name.lower() or search_text.lower() in data['phone'].lower():
                found_contacts.append(f"Контакт {name}: {data['phone']}")
        return found_contacts

    def save_data(self, file_path="data.json"):
        """Збереження даних у файл JSON."""
        with open(file_path, "w") as file:
            json.dump(self.contacts, file)

    def load_data(self, file_path="data.json"):
        """Завантаження даних з файлу JSON."""
        try:
            with open(file_path, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            # Обробка винятку, якщо файл не знайдено
            print("Файл з даними не знайдено.")