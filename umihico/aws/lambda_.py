

import requests as _requests
import json as _json
import functools as _functools
import pprint as _pprint
import traceback as _traceback


def trigger_via_apigateway(url, api_key=None, payload=None):
    method = "POST" if payload else "GET"
    kw = {}
    if api_key:
        kw['headers'] = {'x-api-key': api_key, }
    if payload:
        kw['data'] = _json.dumps(payload)
    return _requests.request(method, url, **kw)


def apigateway_wrapper(lambda_handler):
    @_functools.wraps(lambda_handler)
    def lambda_handler_wrapper(event, context):
        try:
            body = lambda_handler(event, context)
            statusCode = 200
        except Exception as e:
            statusCode = 500
            _traceback.print_exc()
            body = _traceback.format_exc()
        # finally:
        return {"statusCode": statusCode, "body": str(body)}
    return lambda_handler_wrapper


@apigateway_wrapper
def lambda_handler(event, context):
    raise
    # return 'test'


if __name__ == '__main__':
    """
    returns "test!" if lambda_handler is like this.

    def test_trigger_via_apigateway():
        payload = {
            "api_key": "test!",
        }
        # not valid url and key, don't worry
        url = "https://k0ch7iuaj4.execute-api.us-west-2.amazonaws.com/default/asyc_superfast_receiver"
        api_key = "JJnYqNMTBU1LdIEjaSYL43G4OGfysL9B1In5oPoy"
        return trigger_via_apigateway(url, api_key, payload)
    import ast
    def lambda_handler(event, context):
        payload = ast.literal_eval(event['body'])
        return {
            "statusCode": 200,
            "body": payload['api_key']
        }
    """
    print(lambda_handler(None, None))
