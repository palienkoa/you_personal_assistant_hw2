# Модуль Книга записів

from collections import UserDict
from datetime import date, datetime, timedelta
import os
import re
import json


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
    # реалізація клас
    pass

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
                return self.phone
            else:
                print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
                phone = input()
                
                
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
                return self.email
            else:
                print("Введіть електронну адресу латинськими літерами у такому форматі: name@name.name, натисність Enter: ")
                email = input()


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
                
    # реалізація класу
        
    def add_phone(self, phone):                
        
        self.phone = phone                 
        Phone.validate(self, self.phone)
        
        self.phones.append(self.phone)  
            
        phones_ = self.phones        
        return phones_
    
    def days_to_birthday(self, birth_yer, birth_mont, birth_day):
        txt_valid = ' '
        day_now = date.today() 
        rik = day_now.year
        self.birth_yer = birth_yer
        
        self.birth_mont = birth_mont
        
        self.birth_day = birth_day
        
        try:
            birth = date(rik, self.birth_mont, self.birth_day)        
            dniv = int((birth - day_now).days)
            if dniv == 0:
                print(f'Сьогодні день народження у {Name_}')
            if dniv < 0:    
                print(f'У цьому році день народження у {Name_} вже минув')     
            if dniv > 0:
                print(f'До дня народження {Name_} залишилося днів - {dniv}')   
            birth = date(self.birth_yer, self.birth_mont, self.birth_day)
        except ValueError:
            Birthday.validate(self, txt_valid)
            print(self.txt_valid)
            birth = []          
        return birth                 
    
    
    def add_email(self, email):                
        
        self.email = email                 
        Email.validate(self, self.email)
       
        self.emails.append(self.email)      
       
        emails_ = self.emails        
        return emails_
    
    def add_adress(self, adress):                
        
        self.adress = adress                 
        
        adress_ = self.adress        
        return adress_ 
        
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
    
    def __init__(self, data, phones):
        self.data = data        
        self.phones = phones
        file_name = 'data.json'
        with open(file_name, "r") as fh:        
            unpacked = json.load(fh)    
            self.data = unpacked               
            
    def add_record(self, *argv, **kwarg):           
                    
        self.data.update({Name_: phones_, Name_+'_день народження': str(birth_), Name_+'_Email': emails_, Name_+'_Адреса': adress_}) 
        
        file_name = 'data.json'        
        with open(file_name, "w") as fh:
            json.dump(self.data, fh)  
        
        if flag_new == 1:
            return
                
            
    def find(self, name):
        if name in self.data:
            return name       
        
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
            self.data.pop(rec+'_день народження')
            self.data.pop(rec+'_Email')
            self.data.pop(rec+'_Адреса')
        except KeyError:
            print("Немає такого імені")
            return
        
        a_ = f'DELETED RECORD {rec}'
        print(a_)
        
        file_name = 'data.json'        
        with open(file_name, "w") as fh:
            json.dump(self.data, fh)          
                
    def iterator(self, item_number):
        self.item_number = item_number               
        counter_ = 0
        counterr_ = 0
        resultt = ''
        len_data = len(self.data)
        
        for item_, recordd in self.data.items():            
            resultt += f'{item_}: {recordd} \n'   
            counter_ += 1
            counterr_ += 1
            if  counterr_ == len_data:
                print(resultt)
                return
            if counter_ == self.item_number:                
                print(resultt)         
                counter_ = 0
                resultt = ''
                print('Продовжити перегляд? Натисніть ENTER')
                inp = input()
        
    
        # Створення нової адресної книги
data = {}
phones = []
phones_ = []
phone = ''
birth = []
email = ''
emails = []
emails_ = []
adress_ = ' '
adress = ' '
flag_new = 0

book = AddressBook(data, phones)

    # Створення першого зразкового запису для Приклад_запису_прізвище
john_record = Record("Ім'я")
Name_ = john_record.name.value
john_record.add_phone("1234567890")
phones_ = john_record.add_phone("0987654321")
birth_ = john_record.days_to_birthday(2050, 12, 23)
john_record.add_email("a.name@gmail.com")
emails_ = john_record.add_email("a.name@knu.ua")
adress_ = john_record.add_adress("Київ, вул. Київська, 1")

    # Додавання запису Ім'я до книги контактів
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# Name_ = jane_record.name.value
# phones_ = jane_record.add_phone("9876543210")
# birth_ = jane_record.days_to_birthday(1950, 11, 21)
# book.add_record(jane_record)

    # Виведення всіх записів у книзі
print('Перегляд усіх записів за пошуковим словом')
nme = input()
for name, record in book.data.items():
    if nme in name or nme in record:
        print('ЗНАЙДЕНО ЗАПИС: ')
        print(name, record)

    # Знаходження та редагування телефону для John
# john = book.find("John")
# john_record.edit_phone("1234567890", "1112223333")
# print('Зроблено заміну телефона для ', john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
# found_phone = book.find_phone('5555555555')
# print(f"'Знайдено телефон для ' {john}: {found_phone}")  # Виведення: 5555555555
# phones_ = john_record.remove_phone("1112223333")

    # Видалення запису Jane
# book.delete("Jane")

# ЗАПОВНЕННЯ КНИГИ КОНТАКТІВ
while True:
    flag_new = 1
    print(' ')
    print('Заповнити книгу контактів? - Enter\nПереглянути книгу? - r + Enter\nВидалити запис? - d + Enter\nРедагувати запис? - ed + Enter\nВийти? - q + Enter')
    inp = input()
    if inp == 'q':        
        os.abort()
        
    if inp == 'r':
            
    # ПОСТОРІНКОВИЙ ПЕРЕГЛЯД КНИГИ КОНТАКТІВ
        book.iterator(10)  
        continue   
    
    if inp == 'd':
        print("Введіть ім'я для видалення запису")
        imia = input()
        book.delete(imia)
        continue

    new_name = ''
    new_phone = ''
    birth_yer = 0
    birth_mont = 0
    birth_day = 0
    new_email = ''
    new_adress = ' '
    
    print("Введіть ім'я та натисність Enter: ")
    new_name = input()
    
    new_record = Record(new_name)
    Name_ = new_record.name.value
        
    print("Введіть номер телефона без пробілів, символів, має бути 10 цифр, натисність Enter: ")
    new_phone = input()

    phones_ = new_record.add_phone(new_phone)
    
    print("Введіть дату народження.")
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("Рік? (чотири цифри + Enter): ")
        try:
            birth_yer = int(input())
        except ValueError:
            continue
        break
   
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("Місяць? (дві цифри + Enter): ")
        try:
            birth_mont = int(input())
        except ValueError:
            continue
        break
    
    int_ = 0
    while int_ != 1000:        
        int_ += 1
        print("День? (дві цифри + Enter): ")
        try:            
            birth_day = int(input())
        except ValueError:
            continue
        break 
    
    birth_ = new_record.days_to_birthday(birth_yer, birth_mont, birth_day)
    
    print("Введіть електронну адресу латинськими літерами у такому форматі: name@name.name, натисність Enter: ")
    new_email = input()      
    emails_ = new_record.add_email(new_email)    
    
    print("Введіть адресу в довільному форматі та натисність Enter: ")
    new_adress = input()
    adress_ = new_record.add_adress(new_adress)  
    
    book.add_record(new_record)