import requests as _requests

_base_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36", }


def get(url, header_lang="ja,en-US;q=0.9,en;q=0.8", proxy=None):
    headers = _base_headers.copy()
    if header_lang:
        headers['Accept-Language'] = header_lang
    headers['Host'] = urlparse(url).netloc
    kw = {"headers": headers, }
    if proxy:
        kw['proxies'] = {'http': 'http://' + proxy,
                         'https': 'http://' + proxy, }
    return _requests.get(url, **kw)
