import os
import shutil
class FileManager:
    def __init__(self, base_folder: str) -> None:
        self.base_folder = base_folder
    def sort_files(self) -> None:
        for filename in os.listdir(self.base_folder):
            file_path = os.path.join(self.base_folder, filename)
            if os.path.isfile(file_path):
                category = self._get_category(filename)
                category_folder = os.path.join(self.base_folder, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                new_file_path = os.path.join(category_folder, filename)
                shutil.move(file_path, new_file_path)
                print(f"Moved {filename} to {category}")
    def _get_category(self, filename: str) -> str:
        extension = os.path.splitext(filename)[1].lower()
        category_mapping = {
            '.jpg': 'images',
            '.jpeg': 'images',
            '.png': 'images',
            '.gif': 'images',
            '.doc': 'documents',
            '.docx': 'documents',
            '.txt': 'documents',
            '.mp4': 'videos',
            '.avi': 'videos',
            '.mkv': 'videos',
        }
        return category_mapping.get(extension, 'other')