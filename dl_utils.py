#dl_utils.py contains utility functions used in the dl-summer project.
import os

def setup_folder_defaults():
    create_directory_if_not_exists('models')
        
def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'Created directory: {path} ...')