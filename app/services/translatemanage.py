# from pdf2zh import translate, translate_stream # 현재 Python API을 지원하고 있지 않음.

# from app.common.config import DEEPL_API_KEY, OPENAI_API_KEY
import os
import subprocess


async def translate_(service, document):
    cmd = ["pdf2zh", "example.pdf", "-s", f"{service}", "-li", "EN", "-lo", "KO"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except Exception as e:
        print(f"오류 발생: {e}")  # 에러 메시지 출력