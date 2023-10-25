import boto3

s3 = boto3.client('s3')
s3.upload_file('/Users/kylematthews/bucket-chicken.webp', 'my-bucket-of-chicken', 'fried/bucket-chicken.webp')