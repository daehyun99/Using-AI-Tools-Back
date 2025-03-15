from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile

from app.services.translatemanage import translate_
from app.models import TranslateService

from fastapi.responses import FileResponse


router = APIRouter(prefix="/translate")


@router.put("/v1/")
async def translate(service: TranslateService):
    """
    `Translate API`
    :param file:
    :return:
    """
    try:
        await translate_(service)
    except:
        ...
