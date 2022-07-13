
def sanitise_url_for_redirect(url: str) -> str:
    if url.startswith('https://') or url.startswith('http://') or url.startswith("ftp://"):
        return url.strip()

    else:
        return f'http://{url.strip()}'
