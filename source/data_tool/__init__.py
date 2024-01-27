import os
from search import data_search
# TODO from .data_parser

if __name__ == "__main__":
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    print(f"***Init data search in directory: {parent_dir}")
    data = data_search(parent_dir)
