#клас нотатки, майже нічого сам не робить, може тільки зробити пошук за заголовком/тілом
#title - заголовок нотатки, строка
#body - тіло нотатки, строка
#tags - множина тегів строково типу, множина щоб не можна було декілька однакових тегів додати
class Note:
    def __init__(self, title:str, body:str = "", tags:set = None) -> None:
        self.title = title
        self.body = body
        if tags:
            self.tags.update(tags)
        else:
            self.tags = set()

    #шукаємо вказаний текст у заголовку і тілі нотатки, якщо знайшли повертаємо True, інакше - False
    def search(self, search_text:str):
        if search_text in self.title or search_text in self.body:
            return True
        else:
            return False
        

#клас нотатника, робить всі необхідні дії пов"язані з нотатками + робота з тегами
#notes - словник де ключ це заголовок нотатки, а значення сам об"єкт нотатки
#tags_dictionary - словник тегів, ключ це тег, а значення це список з заголовками нотаток з таким тегом,
# наприклад {"рецепти":[борщ,банош]}. Для зручного пошуку всіх нотаток за тегом
class Notes:
    def __init__(self) -> None:
        self.notes = dict()
        self.tags_dictionary = dict()

    #додає нотатку у словник, заголовок буде ключем, сам об"єкт нотатки - значенням.
    def add_note(self, note:Note):
        self.notes.update({note.title:note})
    
    #знаходить нотатку за заданою строкою, якщо знайшли повертає об"єкт нотатки, якщо ні - None
    def find_note(self, search_text:str):
        for note in self.notes:
            if note.search(search_text):
                return note
            else:
                return None

    #службовий метод, при додаванні тега у нотатку також оновлює словник тегів/нотатків нотатника        
    def _add_to_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).update(title)
        else:
            self.tags_dictionary.update({tag:[title,]})
    
    #службовий метод, при видаленні нотатку також видаляє запис зі словника тегів/нотатків нотатника
    def _delete_from_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).pop(title)

    #шукає нотатку з таким заголовком і додає тег, повертає строку з описом результату        
    def add_tag(self, title:str, tag:str):
        
        found_note = self.notes.get(title)
        if found_note != None:
            self.notes.get(title).tags.add(tag)
            self._add_to_tags_dictionary(tag, title)
            return f"Tag {tag} succesfully added to note {title}"
        else:
            return f"Note '{title}' not found"

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
        if found_note != None:
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


