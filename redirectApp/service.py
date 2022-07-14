import time

from database.repository.short_urls import UrlStoreRepository
from utils import ip, timestamp


def save_click_data(short_url_code: str, ip_of_request: str):
    ip_data: dict = ip.get_info(ip=ip_of_request)
    hour_of_click: str = timestamp.get_hour_from_timestamp(time.time())

    UrlStoreRepository().register_url_hit(short_url_code=short_url_code,
                                          country_code=ip_data.get('country'),
                                          region_name=ip_data.get('region'),
                                          city_name=ip_data.get('city'),
                                          hour_of_click=hour_of_click)
