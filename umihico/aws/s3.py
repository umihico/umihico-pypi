import boto3


def gen_s3(key, secret_key, region_name):
    """
    gen s3 by keys instead of "boto3.resource('s3')"
    when you didn't do "aws configure" well
    """
    s3 = boto3.session.Session(
        key=key, secret_key=secret_key, region_name=region_name).resource('s3')
    return s3


def download_text(bucketname, path, s3=None):
    s3 = s3 or boto3.resource('s3')
    obj = s3.Object(bucketname, path)
    text = obj.get()['Body'].read().decode('utf-8')
    return text


def upload_text(bucketname, path, text, public_read=False, ContentType='text/plain', s3=None):
    s3 = s3 or boto3.resource('s3')
    acl = {True: "public-read",
           False: "private"}[public_read]
    response = s3.Bucket(bucketname).put_object(ACL=acl, Body=text,
                                                Key=path, ContentType=ContentType)
