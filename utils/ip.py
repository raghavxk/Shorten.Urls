import requests
from env import ENV
from typing import Optional
API_TOKEN = ENV.ip_info_api_key


def get_country(ip: str) -> Optional[str]:
    """
    This function returns the country of origin of IP.
    """
    resp = requests.get(url=f"https://ipinfo.io/{ip}/json?token={API_TOKEN}")
    if resp.status_code//10 == 20:
        if 'bogon' in resp.json():
            return "DEV"
        return resp.json()['country']
    else:
        return None
