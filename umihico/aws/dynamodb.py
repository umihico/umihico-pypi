

import boto3 as _boto3


def put_item(tablename, dict_):
    dynamodb = _boto3.resource('dynamodb')
    table = dynamodb.Table(tablename)
    return table.put_item(Item=dict_)


def get_item(tablename, dict_):
    dynamodb = _boto3.resource('dynamodb')
    table = dynamodb.Table(tablename)
    response = table.get_item(Key=dict_)
    return response['Item']


def list_all_tabel_names():
    dynamodb = _boto3.resource('dynamodb')
    table_list = dynamodb.tables.all()
    for table in table_list:
        print(table.table_name)


if __name__ == '__main__':
    list_all_tabel_names()
    dict_ = {'request_id': 0, 'chunk_id': 0, 'value': ['bbb', 'rcoy']}
    print(put_item('requests_superfast_dynamo', dict_))
    dict_ = {'request_id': 0, 'chunk_id': 0}
    item = get_item('requests_superfast_dynamo', dict_)
    print(item)
    print(item['value'])
    print(type(item['value']))
