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
        "find-contact",
        "edit-contact",
        "del-contact",
        "show-all",
        "add-phone",
        "add-email",
        "add-address",
        "add-birthday",
        "edit-phone",
        "edit-email",
        "del-phone",
        "del-email",
        "del-address",
        "del-birthday",
        "next-birthdays",
        #notes section, del comment later
        "add-note",
        "find-note",
        "del-note",
        "show-notes",
        "add-tag",
        "find-tag",
        "sort-tag",
        "show-all-tags",       
        "sort-tag",        
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
            elif choice == "edit-contact":
                self.edit_contact()
            elif choice == "find-contact":
                self.find_contact()
            elif choice == "del-contact":
                self.add_phone()
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
            elif choice == "edit-phone":
                self.edit_phone()
            elif choice == "edit-email":
                self.edit_email()
            elif choice == "del-phone":
                self.del_phone()
            elif choice == "del-email":
                self.del_email()
            elif choice == "del-address":
                self.del_address()
            elif choice == "del-birthday":
                self.del_birthday()
            elif choice == "next-birthdays":
                self.show_next_birthdays()
            #КОМАНДИ НОТАТОК
            #HHHHHHHHHHHHHHH
            elif choice == "add-note":
                self.add_note()
            elif choice == "find-note":
                self.find_note()
            elif choice == "del-note":
                self.del_note()
            elif choice == "add-tag":
                self.add_tag()
            elif choice == "find-tag":
                self.find_tag()
            elif choice == "sort-tag":
                self.sort_tag()
            elif choice == "show-notes":
                self.show_notes()
            elif choice == "show-all-tags":
                self.show_all_tags()
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
            if len(name.strip()) < 3:
                print('Ім\'я повинно складатися з більше ніж 2 символів')
            else:
                break
        contact = Record(name)
        while True:
            address = input("Введіть адресу контакту: ").strip()
            if len(name.strip()) < 3:
                print('Адреса повинна складатися з більше ніж 2 символів')
            else:
                break
        while True:
            phone = input("Введіть номер телефону контакту: ").strip()
            if not contact.validate_phone(phone):
                console.print("Неправильний формат.\nВведіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter", style='bold red')
            else:
                break
        while True:
            email = input("Введіть email контакту: ").strip()
            if not contact.validate_email(email):
                console.print("Введіть електронну адресу латинськими літерами у такому форматі: name@name.name, натисність Enter: ", style='bold red')
            else:
                break
        birthday = input("Введіть день народження контакту (рррр-мм-дд): ")
        note = input("Введіть примітку для контакту: ")

        contact.add_adress(address)
        contact.add_phone(phone)
        contact.add_email(email)
        contact.add_birthday(birthday)
        contact.add_note(note)
        
        self.address_book.add_record(contact)
        # self.save_data()
    
    def find_contact(self):
        records_completer = WordCompleter(list(self.address_book.data.keys()))
        name = prompt("Введіть строку для пошуку контакту: ", completer=records_completer)
        contacts = self.address_book.find(name)
        if contacts:
            table = Table(show_header=True, header_style="bold red")
            table.add_column("Iм'я", style="dim", width=10) # ширину можете міняти, назви колонок також
            table.add_column("Телефони", width=25)
            table.add_column("Імейли", justify="left")
            table.add_column("Адреса", justify="left")
            table.add_column("День народження", justify="left")
            table.add_column("Примітка", justify="left")
            
            for contact in contacts:
                table.add_row(contact.name.value, ",".join(contact.phones), ",".join(contact.emails), contact.adress, contact.birthday, contact.note)
                table.add_section()
                # print(contact)
            console.print(table)
        else:
            print("Нічого не знайдено.")
            
    def edit_contact(self):
        #TODO
        pass
    
    def del_contact(self):
        #TODO
        pass

    def show_contacts(self):
        contacts = list(self.address_book.data.values())
        if contacts:
            table = Table(show_header=True, header_style="bold red")
            table.add_column("Iм'я", style="dim", width=10) # ширину можете міняти, назви колонок також
            table.add_column("Телефони", width=25)
            table.add_column("Імейли", justify="left")
            table.add_column("Адреса", justify="left")
            table.add_column("День народження", justify="left")
            table.add_column("Примітка", justify="left")
            
            for contact in contacts:
                table.add_row(contact.name.value, ",".join(contact.phones), ",".join(contact.emails), contact.adress, contact.birthday, contact.note)
                table.add_section()
                # print(contact)
            console.print(table)
        else:
            print("Немає жодного контакту.")
    
    def add_phone(self):
        while True:
            contact_name = input("Введіть ім'я контакту: ")#.capitalize()        
            contact = self.address_book.find(contact_name)
            if contact:
                phone = input("Введіть номер телефону: ")
                if contact.validate_phone(phone):
                    contact.add_phone(phone)
                    print("Номер телефону успішно доданий.")
                    break
                else:
                    print("Не коректні ввелення, спробуйте ще раз") 
            else:
                print("Ім'я контакту не знайдено")
    
    def add_email(self):
        while True:
            contact_name = input("Введіть ім'я контакту: ")#.capitalize()
            contact = self.address_book.find(contact_name)
            if contact:
                email = input("Додайте електронну адресу: ")
                if contact.validate_email(email):
                    contact.add_email(email)
                    print("Електронну адресу успішно додано")
                    break
                else:
                    print("Не коректні ввелення, спробуйте ще раз")
            else:
                print("Ім'я контакту не знайдено")
    
    def add_address(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, АДРЕСУ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ АДРЕСУ (ХЗ, ХОЧА Б НА ДОВЖИНУ СТРОКИ, МІНІМУМ 3 СИМВОЛИ). ДОДАТИ АДРЕСУ КОНТАКТУ
        pass
    
    def add_birthday(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ДАТУ НАРОДЖЕННЯ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ ДАТУ. ДОДАТИ ДАТУ НАРОДЖЕННЯ КОНТАКТУ
        pass
    
    def edit_phone(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ТЕЛЕФОН, НОВИЙ ТЕЛЕФОН. ЗНАЙТИ КОНТАКТ. ЗНАЙТИ ТЕЛЕФОН. ВАЛІДУВАТИ НОВИЙ ТЕЛЕФОН. ЗМІНИТИ ТЕЛЕФОН КОНТАКТУ
        pass
    
    def edit_email(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ІМЕЙЛ, НОВИЙ ІМЕЙЛ. ЗНАЙТИ КОНТАКТ. ЗНАЙТИ ІМЕЙЛ. ВАЛІДУВАТИ НОВИЙ ІМЕЙЛ. ЗМІНИТИ ІМЕЙЛ КОНТАКТУ
        pass
    
    def del_phone(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ТЕЛЕФОН, НОВИЙ ТЕЛЕФОН. ЗНАЙТИ КОНТАКТ. ЗНАЙТИ ТЕЛЕФОН. ВАЛІДУВАТИ НОВИЙ ТЕЛЕФОН. ЗМІНИТИ ТЕЛЕФОН КОНТАКТУ
        pass
    
    def del_email(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ІМЕЙЛ, НОВИЙ ІМЕЙЛ. ЗНАЙТИ КОНТАКТ. ЗНАЙТИ ІМЕЙЛ. ВАЛІДУВАТИ НОВИЙ ІМЕЙЛ. ЗМІНИТИ ІМЕЙЛ КОНТАКТУ
        pass
    
    def del_address(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, АДРЕСУ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ АДРЕСУ (ХЗ, ХОЧА Б НА ДОВЖИНУ СТРОКИ, МІНІМУМ 3 СИМВОЛИ). ДОДАТИ АДРЕСУ КОНТАКТУ
        pass
    
    def del_birthday(self):
        #TODO
        #ЗАПИТАТИ ІМ"Я, ДАТУ НАРОДЖЕННЯ. ЗНАЙТИ КОНТАКТ. ВАЛІДУВАТИ ДАТУ. ДОДАТИ ДАТУ НАРОДЖЕННЯ КОНТАКТУ
        pass 
    
    def show_next_birthdays(self):
        # file_name = 'data.json'
        # with open(file_name, "r", encoding='utf-8') as fh:
        #     unpacked = json.load(fh)
        dniv_ = input("Введіть кількість днів: ")
        # day_now = date.today()
        # rik = day_now.year
        # db = "_день народження"
        # for key_birth, val_birth in unpacked.items():
        #     if db in key_birth:
        #         ind = key_birth.index(db)
        #         name_birth = key_birth[0:ind]
        #         misiac = int(val_birth[5:7])
        #         den = int(val_birth[8:10])
        #         data_birth_1 = date(rik, misiac, den)
        #         dniv = int((data_birth_1 - day_now).days)
        #         if dniv <= int(dniv_) and dniv > 0:
        #             console.print(f'До дня народження [red]{name_birth}[/red] залишилося днів - {dniv}', style='bold green') 
        console.print(f'В настіпні [red]{dniv_}[/red] днів, немає днів народжень', style='bold green')   

        #МЕТОДИ НОТАТОК
        #ННННННННННННННННННННННННННННННННННН
    def add_note(self):
        title = input("Введіть назву нотатки: ")
        content = input("Введіть текст нотатки: ")
        #тут треба перевірки що ввели хоч щось
        new_note = Note(title, content)
        self.notebook.add_note(new_note)
        print("Нотатка успішно додана.")
    
    def find_note(self):
        notes_completer = WordCompleter(list(self.notebook.notes.keys()))
        name = prompt("Введіть строку для пошуку нотатки: ", completer=notes_completer)
        result = self.notebook.find_note(name)
        #прописування колонок
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ЗАГОЛОВОК", style="dim", width=10) # ширину можете міняти, назви колонок також
        table.add_column("НОТАТКА", width=25)
        table.add_column("ТЕГИ", justify="left")
        if not result:
            print("Записи не знайдено")
        else:
            for note in result:
                table.add_row(note.title, note.body, ",".join(list(note.tags)))
                table.add_section()

        console.print(table)    
        # print(result)
    
    def del_note(self):
        notes_completer = WordCompleter(list(self.notebook.notes.keys()))
        name = prompt("Введіть назву нотатки для видалення: ", completer=notes_completer)
        self.notebook.delete_note(name)

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
                table.add_row(note.title, note.body, ",".join(list(note.tags)))
                table.add_section()

            console.print(table)
            
    def add_tag(self):
        notes_completer = WordCompleter(list(self.notebook.notes.keys()))
        name = prompt("Введіть імя нотатки: ", completer=notes_completer).strip()
        result = self.notebook.find_note(name)
        if result:
            tags_completer = WordCompleter(list(self.notebook.tags_dictionary.keys()))
            tag = prompt("Введіть тег: ", completer=tags_completer).strip()
            self.notebook.add_tag(name, tag)
    
    def find_tag(self):
        tags_completer = WordCompleter(list(self.notebook.tags_dictionary.keys()))
        tag = prompt("Введіть тег: ", completer=tags_completer).strip()
        result = self.notebook.search_by_tag(tag)
        if not len(result):
            print('Такого тегу в базі даних немає')
            return
        #прописування колонок
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ЗАГОЛОВОК", style="dim", width=10) # ширину можете міняти, назви колонок також
        table.add_column("НОТАТКА", width=25)
        table.add_column("ТЕГИ", justify="left")
        
        for note in result:
            table.add_row(note.title, note.body, ",".join(list(note.tags)))
            table.add_section()

        console.print(table)
        
    
    def sort_tag(self):
        result = self.notebook.sort_by_tags()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ЗАГОЛОВОК", style="dim", width=10) # ширину можете міняти, назви колонок також
        table.add_column("НОТАТКА", width=25)
        table.add_column("ТЕГИ", justify="left")
        
        for note in result:
            table.add_row(note.title, note.body, ",".join(list(note.tags)))
            table.add_section()

        console.print(table)
        
    def del_tag(self):
        tags_completer = WordCompleter(list(self.notebook.tags_dictionary.keys()))
        tag = prompt("Введіть тег: ", completer=tags_completer).strip()
        # self.notebook.delete_tag(tag)
        print(f"Тег {tag} видалено")#не готово
    
    def show_all_tags(self):
        print(self.notebook.get_all_tags())

if __name__ == "__main__":
    console_interface = ConsoleInterface()
    console_interface.run()    