import boto3

try:
    s3 = boto3.client('s3')
    s3.copy_object(Bucket='my-boto3-bucket-lola', Key='fried/bucket-chicken.webp', CopySource='my-bucket-of-chicken/fried/bucket-chicken.webp')

except NoCredentialsError:
    print('AWS credentials not found, please try again.')

except ClientError:
    if ClientError.response['Error']['Code'] == 'NoSuchBucket':
            print('The specified bucket does not exist.')
    else:
        print('An error occured:', e)

s3.delete_object(Bucket='my-boto3-bucket-lola', Key='fried/bucket-chicken.webp')