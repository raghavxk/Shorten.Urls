import time

from database.repository.short_urls import UrlStoreRepository
from utils import ip, timestamp


def save_click_data(short_url_code: str, ip_of_request: str):
    country_of_origin: str = ip.get_country(ip_of_request)
    hour_of_click: str = timestamp.get_hour_from_timestamp(time.time())
    print(hour_of_click)
    UrlStoreRepository().register_url_hit(short_url_code=short_url_code,
                                          country_code=country_of_origin,
                                          hour_of_click=hour_of_click)
