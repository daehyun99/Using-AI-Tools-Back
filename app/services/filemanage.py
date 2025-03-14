import os 

from app.common.config import DOCS_SAVE_PATH, base_dir


def delete_file_(file_path):
    try:
    try:
        os.remove(f'{file_path}')
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error deleting video: {e}")