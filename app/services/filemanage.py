import os
import aiofiles

from app.common.config import DOCS_SAVE_PATH, base_dir
from app.common.response import SuccessResponse
from app.errors import exceptions as ex


def delete_file_(file_path):
    try:
        os.remove(f'{file_path}')
    # except FileNotFoundError:
    #     raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        error_message = ex.ErrorResponse_File(ex=e).to_dict()
        print(error_message)
    

async def upload_file_(file, DOCS_SAVE_PATH=DOCS_SAVE_PATH):

    file_path = f"{DOCS_SAVE_PATH}/{file.filename}"

    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    return file_path


async def rename_file_():
    try:
        ...
        success_message = SuccessResponse().to_dict()
        print(success_message)
    except Exception as e:
        ...
        error_message = ex.ErrorResponse_File(ex=e).to_dict()
        print(error_message)
    