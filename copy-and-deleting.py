import boto3

s3 = boto3.client('s3')
s3.copy_object(Bucket='my-boto3-bucket-lola', Key='fried/bucket-chicken.webp', CopySource='my-bucket-of-chicken/fried/bucket-chicken.webp')