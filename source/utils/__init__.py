from .load_mp3 import load_mp3


class Tool():
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir

    def load_mp3(self, target_dir):
        return load_mp3(self.parent_dir, target_dir)
