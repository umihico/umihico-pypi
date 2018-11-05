

import requests as _requests
import json as _json
import functools as _functools
import pprint as _pprint
import traceback as _traceback
from ..zip import compress_text as _compress_text
from ..zip import decompress_text as _decompress_text
import ast as _ast


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
            body = _traceback.format_exc()
            print(body)
        return {"statusCode": statusCode, "body": str(body)}
    return lambda_handler_wrapper
