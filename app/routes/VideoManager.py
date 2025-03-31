from fastapi import APIRouter, Depends

from app.models import Video
from app.services.videomanage import download_video_, delete_video_, rename_video_
from app.common.const import VIDEO_SAVE_PATH, DOCS_SAVE_PATH

from app.api.response import SuccessResponse
from app.api import exceptions as ex

from app.database.conn import db
from app.services.llm_models import whisperAI_model

from app.services.utils import logging_response
from app.services.utils import generate_metadata

router = APIRouter(prefix="/video")

layer = "PRESENTATION"

@router.post("/download/")
async def download_video(video: Video):
    """
    `Video API`
    :param VideoDownload:
    :return video_path:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        video_path = download_video_(video.url, session=session, correlation_id=correlation_id)
        success_message = SuccessResponse(data={"video_path": video_path.data})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        raise ex.ErrorResponse_Video(ex=e)


@router.put("/rename/")
async def rename_video(video: Video):
    """
    `Video API`
    :param VideoRename:
    :return:
    """
    video_ = None
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        video_ = await rename_video_(video.path, session=session, correlation_id=correlation_id)
        video_ = video_.data
        success_message = SuccessResponse(data={"video_path": video_["video_path"], "video_title": video_["video_title"]})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)


@router.delete("/delete/")
async def delete_video(video: Video):
    """
    `Video API`
    :param VideoDelete:
    :return:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        log = delete_video_(video.path, session=session, correlation_id=correlation_id)
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)