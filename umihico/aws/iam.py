import boto3


def create_user(username):
    # not tested
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    return response
