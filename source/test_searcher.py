import os
from utils import Tool

if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.join(parent_dir, "../")
    target_dir = os.path.join(parent_dir, "loaded_mp3")
    print(f"***Init data search in directory: {parent_dir}")
    tool = Tool(parent_dir)
    print(tool.load_mp3(target_dir))
