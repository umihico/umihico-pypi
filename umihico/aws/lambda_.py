

import requests as _requests
import json as _json
import functools as _functools
import pprint as _pprint
import traceback as _traceback
from ..zip import compress_text as _compress_text
from ..zip import decompress_text as _decompress_text
import ast as _ast
import os as _os


def _get_content_type():
    return _os.getenv('apigateway_decorator_Content_Type', "text/plain")


def set_content_type(content_type="text/html"):
    _os.environ['apigateway_decorator_Content_Type'] = content_type


def event2args(event):
    compressed_text = event['body']
    if compressed_text:
        text = _decompress_text(compressed_text)
        return _ast.literal_eval(text)
    else:
        return []


def args2payload(*args):
    compressed_text = _compress_text(str(args))
    payload = compressed_text
    return payload


def trigger_via_apigateway(url, api_key=None, payload=None):
    method = "POST" if payload else "GET"
    kw = {}
    if api_key:
        kw['headers'] = {'x-api-key': api_key, }
    if payload:
        kw['data'] = _json.dumps(payload)
    return _requests.request(method, url, **kw)


def apigateway_decorator(lambda_handler):
    @_functools.wraps(lambda_handler)
    def lambda_handler_wrapper(event, context):
        try:
            body = str(lambda_handler(event, context))
            statusCode = 200
        except Exception as e:
            statusCode = 500
            body = "\n_____error_log_____\n" + \
                _traceback.format_exc() + "\n_____error_log_____"
            print(body)
        return {"statusCode": statusCode, "headers": {"Content-Type": _get_content_type()}, "body": str(body)}
    return lambda_handler_wrapper
