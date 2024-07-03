"""SD.NEXT Compatibility API V1 routes

"""
from typing import List, Optional
from fastapi import APIRouter, Depends, Header, Query, UploadFile
from fastapi.params import File

from modules.util import HWC3

from fooocusapi.models.common.base import DescribeImageType
from fooocusapi.utils.api_utils import api_key_auth

from fooocusapi.models.common.requests import CommonRequest as Text2ImgRequest
from fooocusapi.models.requests_v1 import (
    ImgUpscaleOrVaryRequest,
    ImgPromptRequest,
    ImgInpaintOrOutpaintRequest
)
from fooocusapi.models.common.response import (
    AsyncJobResponse,
    GeneratedImageResult,
    DescribeImageResponse,
    StopResponse
)
from fooocusapi.utils.call_worker import call_worker
from fooocusapi.utils.img_utils import read_input_image
from fooocusapi.configs.default import img_generate_responses
from fooocusapi.worker import process_stop


secure_router = APIRouter(
    dependencies=[Depends(api_key_auth)]
)


def stop_worker():
    """Interrupt worker process"""
    process_stop()

@secure_router.post(
        path="/api/sd/ping",
        description="Returns a simple 'pong'",
        tags=['Query'])
async def ping():
    """\nPing\n
    Ping page, just to check if the fastapi is up.
    Instant return correct, does not mean the service is available.
    Returns:
        A simple string pong
    """
    return 'pong'

def stop():
    """Interrupt worker"""
    stop_worker()
    return StopResponse(msg="success")
