from database.repository.short_urls import UrlStoreRepository
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
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


@router.get("/{short_url_code}")
def handler_get_url_stats(short_url_code: str):
    """
    Route : GET /url/{shortUrlCode}
    -> returns complete data for supplemented short url code
    """
    try:
        print(short_url_code)
        url_data = UrlStoreRepository().get_original_url_data_from_code(url_code=short_url_code)
        print(url_data)
        if not url_data:
            return JSONResponse(
                content={
                    'msg': 'requested url code does not exist'
                },
                status_code=status.HTTP_404_NOT_FOUND
            )

        return JSONResponse(
            content={
                'data': {
                    'shortUrlCode': url_data.get('_id'),
                    'originalUrl': url_data.get('original_url'),
                    'hourWiseClickCount': url_data.get('hour_wise_click_count'),
                    'countryWiseClickCount': url_data.get('country_wise_click_count')
                },
            },
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            content={
                'success': False,
                'msg': 'failed to fetch data for provided url code'
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
