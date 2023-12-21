from modules.address_book import AddressBook, Record
from modules.notes import Notes, Note
from modules.file_manager import FileManager 
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.table import Table
console = Console()

class ConsoleInterface:
    def __init__(self):
        self.address_book = AddressBook()
        self.address_book.load()
        
        self.notebook = Notes()
        self.notebook.load()
        
    def is_not_empty(self, data):
        # Перевірка, чи дані не є порожніми
        return bool(data)
    
    def help():
        #TODO
        #ПРИНТУВАТИ СПИСОК КОМАНД, МОЖНА ВЗЯТИ ІЗ РІДМІ.МД
        pass
        

    def run(self):
        commands = [
        "add-contact",
        "edit-contact",
        "del-contact",
        "show-all",
        "add-phone",
        "add-email",
        "add-address",
        #notes section, del comment later
        "add-note",
        "all-notes",
        "add-tag",
        "find-notes",
        #other, del later
        "sort-folder",
        "help",
        "bye",
        "exit",
        "quit"
    ]
        command_completer = WordCompleter(commands)

        while True:
            choice = prompt("Введіть команду: ", completer=command_completer)

            #КОМАНДИ АДРЕСНОЇ КНИГИ
            #AAAAAAAAAAAAAAAAAAAAAA
            if choice == "add-contact":
                self.add_contact()
            elif choice == "show-all":
                self.show_contacts()
            elif choice == "add-phone":
                self.add_phone()
            elif choice == "add-email":
                self.add_email()
            elif choice == "add-address":
                self.add_address()
            elif choice == "add-birthday":
                self.add_birthday()
            #КОМАНДИ НОТАТОК
            #HHHHHHHHHHHHHHH
            elif choice == "add-note":
                self.add_note()
            elif choice == "find-notes":
                notes_completer = WordCompleter(list(self.notebook.notes.keys()))
                name = prompt("Введіть строку для пошуку нотатки: ", completer=notes_completer)
                result = self.notebook.find_note(name)
                print(result)
            elif choice == "add-tag":
                self.add_note()
            elif choice == "find-tag":
                self.add_note()
            elif choice == "sort-tag":
                self.add_note()
            elif choice == "show-notes":
                self.show_notes()
            #СОРТУВАННЯ
            elif choice == "sort-folder":
                name = input("Введіть повний шлях до папки: ")
                #додати перевірку правильності шляху, path.exists щось таке. Можливо винести в окрему процедуру, як вище
                fmanager = FileManager(name)
                fmanager.sort_files()
            elif choice in ["bye","exit","quit"]:
                print("Дякую за використання! До побачення.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")
                
        #dump address_book and notebook
        self.address_book.dump()
        self.notebook.dump()

    def add_contact(self):
        while True:
            name = input("Введіть ім'я контакту: ")
            address = input("Введіть адресу контакту: ")
            phone = input("Введіть номер телефону контакту: ")
            email = input("Введіть email контакту: ")
            birthday = input("Введіть день народження контакту (рррр-мм-дд): ")

            if all(self.is_not_empty(data) for data in [name, address, phone, email, birthday]):
                # if all(self.is_valid_input(data) for data in [name, address, phone, email, birthday]):
                break
            # else:
            #     print("Некоректно введені дані. Будь ласка, перевірте правильність вводу.")
            else:
                print("Поле пусте, введіть дані.")

        contact = Record(name)
        contact.add_adress(address)
        contact.add_phone(phone)
        contact.add_email(email)
        
        self.address_book.add_record(contact)
        # self.save_data()

    def show_contacts(self):
        contacts = list(self.address_book.data.values())
        if contacts:
            table = Table(show_header=True, header_style="bold red")
            table.add_column("Iм'я", style="dim", width=10) # ширину можете міняти, назви колонок також
            table.add_column("Телефони", width=25)
            table.add_column("Адреса", justify="left")
            
            for contact in contacts:
                table.add_row(contact.name.value, *contact.phones, contact.adress)
                table.add_section()
                # print(contact)
            console.print(table)
        else:
            print("Немає жодного контакту.")
    
    def add_phone(self):
        contact_name = input("Введіть ім'я контакту: ")#.capitalize()        
        contact = self.address_book.find(contact_name)
        if contact:
            phone_number = input("Введіть номер телефону: ")
            contact.add_phone(phone_number)
            print("Номер телефону успішно доданий.")
        else:
            print("Контакту не існує. Створіть його спочатку.")
    
    def add_email(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ІМЕЙЛ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ ІМЕЙЛ. ДОДАТИ ІМЕЙЛ КОНТАКТУ
        pass
    
    def add_address(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, АДРЕСУ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ АДРЕСУ (ХЗ, ХОЧА Б НА ДОВЖИНУ СТРОКИ, МІНІМУМ 3 СИМВОЛИ). ДОДАТИ АДРЕСУ КОНТАКТУ
        pass
    
    def add_birthday(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ДАТУ НАРОДЖЕННЯ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ ДАТУ. ДОДАТИ ДАТУ НАРОДЖЕННЯ КОНТАКТУ
        pass

    def add_note(self):
        title = input("Введіть назву нотатки: ")
        content = input("Введіть текст нотатки: ")
        #тут треба перевірки що ввели хоч щось
        new_note = Note(title, content)
        self.notebook.add_note(new_note)
        print("Нотатка успішно додана.")

    def show_notes(self):

        if not self.notebook.notes:
            print("Немає жодної нотатки.")
        else:
            #прописування колонок
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ЗАГОЛОВОК", style="dim", width=10) # ширину можете міняти, назви колонок також
            table.add_column("НОТАТКА", width=25)
            table.add_column("ТЕГИ", justify="left")

            for note in self.notebook.notes.values():
                table.add_row(note.title, note.body, str(note.tags))
                table.add_section()

            console.print(table)

if __name__ == "__main__":
    console_interface = ConsoleInterface()
    console_interface.run()    