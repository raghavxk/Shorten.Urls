import hashlib


def generate_hash(url: str) -> str:
    return hashlib.md5(url.encode('utf-8')).hexdigest()[:16]
