from database.repository.short_urls import UrlStoreRepository
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from requests import Response
from utils import hash

from urlApp import schemas

router = APIRouter(prefix="/url", tags=["URLS"])


@router.post("")
def handler_create_url(
        req: schemas.PostReqBody):
    """
    Route : POST /url
    -> generates short url codes for long urls
    """
    try:
        shortened_url_code = hash.generate_hash(req.url)

        saved_data = UrlStoreRepository().save_new_url(
            short_url_code=shortened_url_code, original_url=req.url)

        if not saved_data:
            return JSONResponse(
                content={
                    'success': False,
                    'msg': 'can not register an already registered-url'
                },
                status_code=status.HTTP_406_NOT_ACCEPTABLE
            )

        return JSONResponse(
            content={'info': {
                'originalUrl': req.url,
                'shortenedUrlCode': shortened_url_code
            },
                'success': True
            },
            status_code=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return JSONResponse(content={
            'success': False,
            'msg': 'failed to register url'
        },
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )
