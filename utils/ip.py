import requests
from env import ENV
from typing import Optional
API_TOKEN = ENV.ip_info_api_key


def get_info(ip: str) -> dict:
    """
    This function returns geographical data of ip.
    """
    resp = requests.get(url=f"https://ipinfo.io/{ip}/json?token={API_TOKEN}")
    if resp.status_code//10 == 20:
        if 'bogon' in resp.json():
            return {}
        return resp.json()
    else:
        return {}
