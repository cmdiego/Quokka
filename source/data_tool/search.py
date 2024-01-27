import os
import shutil
import sys


class data_search():
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir

    def find_downloads_dir(self, start_path):
        for root, dirs, files in os.walk(start_path):
            if 'downloads' in dirs:
                return os.path.join(root, 'downloads')
        return None

    def search_and_move(self):
        """Returns addr of loaded mp3 folder"""
        dwnld_dir = self.find_downloads_dir(self.parent_dir)
        if dwnld_dir is None:
            sys.exit("Error data_search: No downloads folder found")
        # storage addr name loaded_mp3
        target_dir = os.path.join(self.parent_dir, "/loaded_mp3")
        try:
            os.makedirs(target_dir, exist_ok=True)
        except OSError as error:
            print(f"Failed to create folder {target_dir}, error: {error} = ")
        print(f'***Searching for MP3 files...\n {dwnld_dir}')
        for root, dirs, files in os.walk(dwnld_dir):
            for file in files:
                if file.endswith(".mp3"):
                    mp3_file_path = os.path.join(root, file)
                    # Move the file
                    shutil.move(mp3_file_path, target_dir)
                    print(f"Moved: {mp3_file_path} -> {target_dir}")
        return target_dir
