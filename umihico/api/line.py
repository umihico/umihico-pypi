import requests as _requests
import os as _os


def send_line(message, receiver_api_key=None):
    """
    How to get api key:
    https://qiita.com/iitenkida7/items/576a8226ba6584864d95
    return requests.post()
    """
    receiver_api_key = receiver_api_key or _os.getenv('umihico_line_api_key')
    if not receiver_api_key:
        raise Exception('receiver_api_key is not defined')
    url = "https://notify-api.line.me/api/notify"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Authorization": "Bearer " + receiver_api_key}
    data = {"message": message}
    response = _requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response
