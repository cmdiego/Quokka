import os
import shutil


def find_downloads_dir(path):
    for root, dirs, files in os.walk(path):
        if 'downloads' in dirs:
            return os.path.join(root, 'downloads')
    return None


def load_mp3(path, target_dir):
    """Return true if successfully loaded the mp3 files to target directory"""
    dwnld_dir = find_downloads_dir(path)
    if dwnld_dir is None:
        print(f"Could not find downloads folder in {path}")
        return False
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
                try:
                    shutil.move(mp3_file_path, target_dir)
                except shutil.Error as error:   # Duplicates will trigger this
                    print(f"Failed to move file: {mp3_file_path} -> {target_dir}, reason: {error}")
                print(f"Moved: {mp3_file_path} -> {target_dir}")
    return target_dir
