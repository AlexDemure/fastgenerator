from urllib.parse import urlparse


def checkurl(path: str) -> bool:
    return urlparse(path).scheme in ("http", "https")
