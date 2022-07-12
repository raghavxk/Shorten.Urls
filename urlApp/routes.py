from database.repository.short_urls import UrlStoreRepository
from fastapi import APIRouter, HTTPException, status

from urlApp import schemas
from utils import hash

router = APIRouter(prefix="/url", tags=["URLS"])


@router.post("", status_code=status.HTTP_201_CREATED)
def handler_create_url(
        req: schemas.PostReqBody):
    """
    Route : GET /url
    -> generates short url codes for long urls
    """
    try:
        shortened_url_code = hash.generate_hash(req.url)
        saved_data = UrlStoreRepository().save_new_url(
            short_url_code=shortened_url_code, original_url=req.url)
        return {
            'info': {
                'originalUrl': req.url,
                'shortenedUrlCode': shortened_url_code
            },
            'success': True
        }
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"failed to generate short url"
        )
