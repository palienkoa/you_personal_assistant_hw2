# Модуль Книга записів
from collections import UserDict
from datetime import date, datetime, timedelta
import os
import re
import json
import pickle
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from pathlib import Path
console = Console()

class Field:
    
    def __init__(self, value):
        self.__value = None
        self.value = value
        
    @property    
    def __str__(self):
        return str(self.__value)
    
    @__str__.setter
    def __str__(self):
        return str(self.__value)
       
class Name(Field):
    
    def __str__(self) -> str:
        return super().__str__()

class Phone(Field):
    # реалізація класу
    
    def __init__(self, value):
        
        self.phone = value
        self.validate(value)
        super().__init__(value)            
         
    def validate(self, phone):  
        while True:            
            self.phone = phone            
            long_ = len(self.phone)
            symb = str(self.phone).isnumeric()
            if long_ == 10 and symb == True:
                return True
            else:
                return False                                           
                
class Birthday(Field):
#     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.birth = self.value
        return self.birth     
        
    def validate(self, txt_valid):   
        self.txt_valid = txt_valid         
        self.txt_valid = "Введіть день народження у такому форматі: спочатку РІК, потім місяць ММ, потім день ДД,\nнаприклад: 2000 12 31"
        return self.txt_valid    
    
class Email(Field):
     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.email = self.value
        return self.email       
        
    def validate(self, email):
        while True:
            self.email = email
            name_split = self.email.split('@')
            for n_sp in name_split:
                pass
            len_mail = len(self.email)
            rah_1 = self.email.count('@')
            rah_2 = self.email.count(' ')
            rah_3 = n_sp.count('.')
            rah_4 = self.email.count(',')
            if len_mail > 4 and rah_2 == 0 and rah_1 == 1 and rah_3 > 0 and rah_4 == 0:
                return True
            else:
                return False

class Adress(Field):
     # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)   
    def __str__(self):
        self.adress = self.value
        return self.adress       
      
class Record:  
       
    def __init__(self, name):
        self.name = Name(name)        
        self.phones = []
        self.emails = []
        self.adress = ' '
        self.birthday = ""
        self.note = ""
        
    def search(self, search_text: str) -> bool:
        return search_text in self.name.value or search_text in self.adress or search_text in self.note
                
    def validate_phone(self, phone):
        self.phone = phone
        long_ = len(self.phone)
        symb = str(self.phone).isnumeric()
        if long_ == 10 and symb == True:
            return True
        else:
            return False 

    def validate_email(self, email):         
            self.email = email
            name_split = self.email.split('@')
            for n_sp in name_split:
                pass
            len_mail = len(self.email)
            rah_1 = self.email.count('@')
            rah_2 = self.email.count(' ')
            rah_3 = n_sp.count('.')
            rah_4 = self.email.count(',')
            if len_mail > 4 and rah_2 == 0 and rah_1 == 1 and rah_3 > 0 and rah_4 == 0:
                return True
            else:
                return False



    def add_phone(self, phone):                
        # self.phone = phone                 
        Phone.validate(self, phone)        
        self.phones.append(phone)              

    
    def days_to_birthday(self):
        txt_valid = ' '
        day_now = date.today() 
        rik = day_now.year
        # self.birth_yer = birth_yer        
        # self.birth_mont = birth_mont        
        # self.birth_day = birth_day
        print('')
        console.print('У В А Г А !!!', style='bold red')
        print('')        
        try:
            birth = date(self.birth_day)        
            dniv = int((birth - day_now).days)
            if dniv == 0:
                console.print(f'Сьогодні день народження у [yellow]{self.name}[/yellow]', style='bold blue')
            if dniv < 0:    
                console.print(f'У цьому році день народження у {self.name} вже минув', style='reverse red')     
            if dniv > 0:
                console.print(f'До дня народження [red]{self.name}[/red] залишилося днів - {dniv}', style='bold green')   
            birth = date(self.birth_yer, self.birth_mont, self.birth_day)
        except ValueError:
            Birthday.validate(self, txt_valid)
            print(txt_valid)
            birth = []          
        return birth                
    
    def add_email(self, email):                                
        Email.validate(self, email)
        self.emails.append(email)
    
    def add_adress(self, adress):                
        self.adress = adress
    
    def add_birthday(self, birthday):                
        self.birthday = birthday 
    
    def add_note(self, note):                
        self.note = note              
        
    def remove_phone(self, phone):
        try:
            self.phone = phone        
            self.phones.remove(self.phone)        
            phones_ = self.phones  
            return phones_
        except ValueError:
            dd = f"Телефон {self.phone} відсутній"     
            print(dd)                    
    
    def edit_phone(self, a, b):
        index_ = self.phones.index(a)
        self.phones[index_] = b        
        pass    
          
    def __str__(self):       
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def __init__(self):
        self.file = "address_book.data"
        self.data = {}               
             
    def add_record(self, record):
        self.data[record.name.value] = record 
                        
    def find(self, search_text):
        found_record = self.data.get(search_text)
        return found_record if found_record else None
    
    def find_records(self, search_text):
        found_records = []
        for record in self.data.values():
            if record.search(search_text):
                found_records.append(record)
        return found_records      
        
    def find_phone(self, ph_):        
        for dict_ in self.data.items():            
            count_ = str(dict_).count(str(ph_))            
            if count_ > 0:                
                return ph_
            if count_ == 0:
                print('Телефон не знайдено')
                return
            else:
                continue                 
    
    def delete(self, rec):        
        try:
            self.data.pop(rec)
        except KeyError:
            print("Немає такого імені")
            return        
        a_ = f'[red]DELETED RECORD[/red] {rec}'
        console.print(a_)        
    
    def dump(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.data, file)
            
    def load(self):
        p = Path(self.file)
        if not p.exists():
            return
        with open(self.file, 'rb') as file:
            try:
                unpacked = pickle.load(file)
                self.data = unpacked
            except EOFError:
                pass #no data saved           