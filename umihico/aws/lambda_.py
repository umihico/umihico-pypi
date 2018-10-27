

import requests as _requests
import json as _json


def trigger_via_apigateway(url, api_key=None, payload=None):
    method = "POST" if payload else "GET"
    kw = {}
    if api_key:
        kw['headers'] = {'x-api-key': api_key, }
    if payload:
        kw['data'] = _json.dumps(payload)
    return _requests.request(method, url, **kw)


if __name__ == '__main__':
    def test_trigger_via_apigateway():
        payload = {
            "prefecture": "栃木",
            "city": "下野",
            "town": "薬師寺"
        }
        url = "https://k0ch7iuaj4.execute-api.us-west-2.amazonaws.com/default/asyc_superfast_receiver"
        api_key = "JJnYqNMTBU1LdIEjaSYL43G4OGfysL9B1In5oPoy"
        return trigger_via_apigateway(url, api_key, payload)

    import ast

    def lambda_handler(event, context):
        """returns "下野"  if lambda_handler is like this."""
        d = ast.literal_eval(event['body'])
        return {
            "statusCode": 200,
            "body": d['city']
        }

    response = test_trigger_via_apigateway()
    print(response.text)
