import boto3
from datetime import datetime
import secret_loader

session_id = datetime.now().strftime('%d%b%Y%H%M%S')
user_client = boto3.client('sts')

r = user_client.assume_role(RoleArn=secret_loader.role_arn, RoleSessionName=session_id, ExternalId=secret_loader.external_id)
s3_client = boto3.client('s3', region_name=secret_loader.aws_region, aws_access_key_id=r['Credentials']['AccessKeyId'], aws_secret_access_key=r['Credentials']['SecretAccessKey'], aws_session_token=r['Credentials']['SessionToken'])
response = s3_client.list_buckets()
print(response)

