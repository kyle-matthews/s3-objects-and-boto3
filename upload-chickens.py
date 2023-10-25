import boto3

try:
    s3 = boto3.client('s3')
    s3.upload_file('/Users/kylematthews/bucket-chicken.webp', 'my-bucket-of-chicken', 'fried/bucket-chicken.webp')
    print('File uploaded successfully.')
except NoCredentialsError:
    print('Incorrect AWS credentials. Please configure and try again.')
except ClientError:
    if ClientError.response['Error']['Code'] == 'NoSuchBucket':
            print('The specified bucket does not exist.')
    else:
        print('An error occured:', e)