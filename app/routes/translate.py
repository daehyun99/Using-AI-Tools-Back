from fastapi import APIRouter

router = APIRouter()


# # ===============
# # test code
from typing import Union

@router.get("/")
def read():
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
