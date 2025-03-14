import os 

from app.common.config import DOCS_SAVE_PATH, base_dir


def delete_file_(file_path, DOCS_SAVE_PATH=DOCS_SAVE_PATH): 
    try:
        os.remove(f'{file_path}')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting video: {e}")