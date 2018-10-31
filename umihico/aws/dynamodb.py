

import boto3 as _boto3


def put_item(tablename, dict_, region_name='us-west-2'):
    dynamodb = _boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table(tablename)
    return table.put_item(Item=dict_)


def get_item(tablename, dict_, region_name='us-west-2'):
    dynamodb = _boto3.resource('dynamodb', region_name=region_name)
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
    dict_ = {'request_id': 8666958513584, 'chunk_id': 0}
    item = get_item('requests_superfast_dynamo', dict_)
    dict_ = {'request_id': 8666958513584, 'chunk_id': 0}
    item = get_item('requests_superfast_dynamo', dict_)
    dict_ = {'request_id': 8666958513584, 'chunk_id': 0}
    item = get_item('requests_superfast_dynamo', dict_)
    dict_ = {'request_id': 8666958513584, 'chunk_id': 0}
    item = get_item('requests_superfast_dynamo', dict_)
    import umihico
    import ast
    compressed_text = item['compressed_text']
    print(ast.literal_eval(umihico.zip.decompress_text(compressed_text)))
