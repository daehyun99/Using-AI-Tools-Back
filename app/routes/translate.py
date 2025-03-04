from fastapi import APIRouter

router = APIRouter()

# <======================>
# # Todo
# 진행상황
# |✅: 완료|⏩: 진행 중|⏸: 중단|⚪: 대기|
# 1. 
# 2. 
# (+) speech2text -> translate 파이프라인 구축 시, speech2text 문서는 PDF 형식이여야 함.
# (+) 번역 API 변경 필요 

# # 관련
# 
# ========================

# <======================>
# # UseCase
# 1. 사용자는 번역할 PDF 문서를 업로드한다.
# 2. 시스템은 번역된 PDF 문서를 제공한다.
# ========================

# # ===============
# # test code
from typing import Union

@router.get("/translate")
def translate_test1():
    return {"Hello": "World"}

@router.get("/translate/items/{item_id}")
def translate_test2(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
