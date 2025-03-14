import os
import aiofiles

from app.common.config import DOCS_SAVE_PATH, base_dir


def delete_file_(file_path):
    try:
        os.remove(f'{file_path}')
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error deleting video: {e}")
    
def upload_file_(file, DOCS_SAVE_PATH=DOCS_SAVE_PATH):

    file_path = f"{DOCS_SAVE_PATH}/{file.filename}"

    with aiofiles.open(file_path, 'wb') as out_file:
        content = file.read()
        out_file.write(content)
    return file_path