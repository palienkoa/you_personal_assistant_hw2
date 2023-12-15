class Note:
    def __init__(self, title:str, body:str, tags:set) -> None:
        self.title = title
        self.body = body
        self.tags.update(tags)

    def search(self, search_text:str):
        if search_text in self.title or search_text in self.body:
            return True
        else:
            return False

class Notes:
    def __init__(self) -> None:
        self.notes = dict()
        self.tags_dictionary = dict()

    def add_note(self, note:Note):
        self.notes.update({note.title:note})
    
    def find_note(self, search_text:str):
        for note in self.notes:
            if note.search(search_text):
                return note
            else:
                return None
            
    def add_to_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).update(title)
        else:
            self.tags_dictionary.update({tag:[title,]})
    
    def delete_from_tags_dictionary(self, tag:str, title:str):
        if tag in self.tags_dictionary.keys():
            self.tags_dictionary.get(tag).pop(title)
            
    def add_tag(self, title:str, tag:str):
        
        found_note = self.notes.get(title)
        if found_note != None:
            self.notes.get(title).tags.update(tag)
            self.add_to_tags_dictionary(tag, title)
            return f"Tag {tag} succesfully added to note {title}"
        else:
            return f"Note '{title}' not found"
        
    def delete_note(self, title:str):
        if title in self.notes.keys():
            for tag in self.notes.get(title).tags:
                self.delete_from_tags_dictionary(tag, title)
            self.notes.pop(title)
            return f"Note {title} sucessfully deleted"
        else:
            return f"Note {title} not found"
        
    def change_note(self, title:str, new_text:str):
        found_note = self.notes.get(title)
        if found_note != None:
            self.notes.get(title).body = new_text
            return f"Note {title} succesfully changed"
        else:
            return f"Note '{title}' not found"  

    def get_all_notes(self):
        return self.notes

note = Note("shopping list", "milk,eggs,cheese")
notes = Notes()
notes.add_note(note)
notes.add_tag(note.title, "recipe")  

