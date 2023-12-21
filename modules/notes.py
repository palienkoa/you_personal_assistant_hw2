class Note:
    def __init__(self, title: str, body: str = "", tags: set = None) -> None:
        self.title = title
        self.body = body
        self.tags = set(tags) if tags else set()

    def search(self, search_text: str) -> bool:
        return search_text in self.title or search_text in self.body

    def __str__(self) -> str:
        return f"{self.title}: {self.body}"


class Notes:
    def __init__(self) -> None:
        self.notes = dict()
        self.tags_dictionary = dict()

    def add_note(self, note: Note) -> None:
        self.notes[note.title] = note
        for tag in note.tags:
            self._add_to_tags_dictionary(tag, note.title)

    def find_note(self, search_text: str) -> Note:
        return next((note for note in self.notes.values() if note.search(search_text)), None)

    def _add_to_tags_dictionary(self, tag: str, title: str) -> None:
        if tag in self.tags_dictionary:
            self.tags_dictionary[tag].append(title)
        else:
            self.tags_dictionary[tag] = [title]

    def _delete_from_tags_dictionary(self, tag: str, title: str) -> None:
        if tag in self.tags_dictionary:
            self.tags_dictionary[tag].remove(title)

    def add_tag(self, title: str, tag: str) -> str:
        found_note = self.notes.get(title)
        if found_note:
            found_note.tags.add(tag)
            self._add_to_tags_dictionary(tag, title)
            return f"Tag '{tag}' successfully added to note '{title}'."
        return f"Note '{title}' not found."

    def search_by_tag(self, tag: str) -> list:
        return [self.notes[title] for title in self.tags_dictionary.get(tag, [])]

    def sort_by_tags(self) -> list:
        sorted_notes = sorted(self.notes.values(), key=lambda note: len(note.tags), reverse=True)
        return sorted_notes

    def delete_note(self, title: str) -> str:
        if title in self.notes:
            for tag in self.notes[title].tags:
                self._delete_from_tags_dictionary(tag, title)
            self.notes.pop(title)
            return f"Note '{title}' successfully deleted."
        return f"Note '{title}' not found."

    def change_note(self, title: str, new_text: str) -> str:
        found_note = self.notes.get(title)
        if found_note:
            found_note.body = new_text
            return f"Note '{title}' successfully changed."
        return f"Note '{title}' not found."

    def get_all_notes(self) -> dict:
        return self.notes

    def get_all_tags(self) -> list:
        return list(self.tags_dictionary.keys())