import json
import pickle
from pathlib import Path
#клас нотатки, майже нічого сам не робить, може тільки зробити пошук за заголовком/тілом
#title - заголовок нотатки, строка
#body - тіло нотатки, строка
#tags - множина тегів строково типу, множина щоб не можна було декілька однакових тегів додати
class Note:
    def __init__(self, title: str, body: str = "", tags: set = None) -> None:
        self.title = title
        self.body = body
        self.tags = set(tags) if tags else set()

    #шукаємо вказаний текст у заголовку і тілі нотатки, якщо знайшли повертаємо True, інакше - False
    def search(self, search_text: str) -> bool:
        return search_text in self.title or search_text in self.body
    
    def __str__(self) -> str:
        return f"{self.title}: {self.body}"
        

#клас нотатника, робить всі необхідні дії пов"язані з нотатками + робота з тегами
#notes - словник де ключ це заголовок нотатки, а значення сам об"єкт нотатки
#tags_dictionary - словник тегів, ключ це тег, а значення це список з заголовками нотаток з таким тегом,
# наприклад {"рецепти":[борщ,банош]}. Для зручного пошуку всіх нотаток за тегом
class Notes:
    def __init__(self) -> None:
        self.file = "notes.data"
        self.tags_file = "tags.data"
        self.notes = dict()
        self.tags_dictionary = dict()

    #додає нотатку у словник, заголовок буде ключем, сам об"єкт нотатки - значенням.
    def add_note(self, note:Note):
        self.notes.update({note.title:note})
        for tag in note.tags:
            self._add_to_tags_dictionary(tag, note.title)
    
    #знаходить нотатку за заданою строкою, якщо знайшли повертає об"єкт нотатки, якщо ні - None
    def find_note(self, search_text:str):
        found_notes = []
        for note in self.notes.values():
            if note.search(search_text):
                found_notes.append(note)
        return found_notes

    #службовий метод, при додаванні тега у нотатку також оновлює словник тегів/нотатків нотатника        
    def _add_to_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).append(title)
        else:
            self.tags_dictionary.update({tag:[title,]})
    
    #службовий метод, при видаленні нотатку також видаляє запис зі словника тегів/нотатків нотатника
    def _delete_from_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).remove(title)

    #шукає нотатку з таким заголовком і додає тег, повертає строку з описом результату        
    def add_tag(self, title:str, tag:str):
        
        found_note = self.notes.get(title)
        if found_note:
            found_note.tags.add(tag)
            self._add_to_tags_dictionary(tag, title)
            return f"Tag {tag} succesfully added to note {title}"
        else:
            return f"Note '{title}' not found"
    
    #method to find notes by tag
    def search_by_tag(self, tag:str):
        found_notes = []
        if tag in self.tags_dictionary.keys():
            for title in self.tags_dictionary.get(tag):
                found_notes.append(self.notes.get(title))
            return found_notes
        else:
            return []

    #виводить список всіх нотатків відсортований за кількістю тегів    
    def sort_by_tags(self):
        sorted_notes = sorted(self.notes.values(), key=lambda note: len(note.tags), reverse=True)
        return sorted_notes

    #шукає нотатку з заданим заголовком, якщо знайшли - видаляємо, повертає строку з описом результату             
    def delete_note(self, title:str):
        if title in self.notes.keys():
            for tag in self.notes.get(title).tags:
                self._delete_from_tags_dictionary(tag, title)
            self.notes.pop(title)
            return f"Note {title} sucessfully deleted"
        else:
            return f"Note {title} not found"

    #шукає нотатку з заданим заголовком, якщо знайшли - замінюємо тіло на новий текст, повертає строку з описом результату                
    def change_note(self, title:str, new_text:str):
        found_note = self.notes.get(title)
        if found_note:
            self.notes.get(title).body = new_text
            return f"Note {title} succesfully changed"
        else:
            return f"Note '{title}' not found"  

    #повертає словник із усіх заголовків/нотаток
    def get_all_notes(self):
        return self.notes

    #повертає список усіх тегів    
    def get_all_tags(self):
        return list(self.tags_dictionary.keys())
    
    def dump(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.notes, file)
        with open(self.tags_file, 'wb') as tags_file:
            pickle.dump(self.tags_dictionary, tags_file)
            
    def load(self):
        p = Path(self.file)
        if not p.exists():
            return
        with open(self.file, 'rb') as file:
            try:
                self.notes = pickle.load(file)
            except EOFError:
                pass #no data saved
        p = Path(self.tags_file)
        if not p.exists():
            return
        with open(self.tags_file, 'rb') as file:
            try:
                self.tags_dictionary = pickle.load(file)
            except EOFError:
                pass #no data saved   
            