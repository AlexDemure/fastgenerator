import urllib.request

from fastgenerator import const


class HTTP:
    @classmethod
    def download(cls, url: str) -> str:
        with urllib.request.urlopen(url) as response:
            return response.read().decode(const.FILE_ENCODING)
