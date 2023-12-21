from modules.address_book import AddressBook
from modules.notes import Notes, Note
from modules.file_manager import FileManager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

class ConsoleInterface:
    def __init__(self):
        self.address_book = AddressBook()
        self.notebook = Notes()
        # тут треба завантаження данних з файлу, щось типу self.notebook.load()

    def run(self):
        commands = [
            "add-contact",
            "add-note",
            "all-notes",
            "show-all",
            "add-phone",
            "add-email",
            "add-address",
            "add-tag",
            "bye",
            "sort-folder"
        ]
        command_completer = WordCompleter(commands)

        while True:
            choice = prompt("Введіть команду: ", completer=command_completer)

            if choice == "add-contact":
                self.add_contact()
            elif choice == "show-all":
                self.show_contacts()
            elif choice == "add-note":
                self.add_note()
            elif choice == "all-notes":
                self.show_notes()
            elif choice == "sort-folder":
                name = input("Введіть повний шлях до папки: ")
                # додати перевірку правильності шляху, path.exists щось таке. Можливо винести в окрему процедуру, як вище
                fmanager = FileManager(name)
                fmanager.sort_files()
            elif choice == "bye":
                print("Дякую за використання! До побачення.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def add_contact(self):
        while True:
            name = input("Введіть ім'я контакту: ")
            address = input("Введіть адресу контакту: ")
            phone = input("Введіть номер телефону контакту: ")
            email = input("Введіть email контакту: ")
            birthday = input("Введіть день народження контакту (рррр-мм-дд): ")

            if all(self.is_not_empty(data) for data in [name, address, phone, email, birthday]):
                if all(self.is_valid_input(data) for data in [name, address, phone, email, birthday]):
                    self.address_book.add_contact(name, phone, email, address, birthday)  # Змінено тут
                    break
                else:
                    print("Некоректно введені дані. Будь ласка, перевірте правильність вводу.")
            else:
                print("Поле пусте, введіть дані.")

    def is_not_empty(self, data):
        # Перевірка, чи дані не є порожніми
        return bool(data)

    def show_contacts(self):
        contacts = self.address_book.list_contacts()
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Немає жодного контакту.")

    def add_note(self):
        title = input("Введіть назву нотатки: ")
        content = input("Введіть текст нотатки: ")
        # тут треба перевірки що ввели хоч щось
        new_note = Note(title, content)
        self.notebook.add_note(new_note)
        print("Нотатка успішно додана.")

    def show_notes(self):
        if not self.notebook.notes:
            print("Немає жодної нотатки.")
        else:
            for note in self.notebook.notes.values():
                print(note)

if __name__ == "__main__":
    console_interface = ConsoleInterface()
    console_interface.run()