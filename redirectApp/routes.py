from http import client
from urllib.request import Request

from database.repository.short_urls import UrlStoreRepository
from fastapi import APIRouter, Request, Response, status
from utils import urls

from redirectApp import service

router = APIRouter(tags=["REDIRECT"])


@router.get("/{short_url_code}")
def handler_redirect(short_url_code: str, request: Request):
    """
    GET /{url_code}
    -> redirects user to required URL
    -> saves click data
    """
    try:
        url_to_redirect_to = UrlStoreRepository().get_original_url_data_from_code(
            short_url_code)['original_url']
        if not url_to_redirect_to:
            return Response(status_code=status.HTTP_404_NOT_FOUND)

        client_ip = request.headers.get('x-forwarded-for')

        url_to_redirect_to = urls.sanitise_url_for_redirect(url_to_redirect_to)

        if client_ip:
            service.save_click_data(
                ip_of_request=client_ip, short_url_code=short_url_code)

        return Response(
            headers={"Location": f"{url_to_redirect_to}"},
            status_code=status.HTTP_307_TEMPORARY_REDIRECT
        )

    except Exception as e:
        print(f"failed to redirect user to url with error : {e}")
        return Response(status_code=status.HTTP_404_NOT_FOUND)
