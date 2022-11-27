
import boto3
def lambda_handler(event, context):

    s3 = boto3.client("s3")
    if event:
         print("event", event)
         file_obj = event["Records"][0]
         filename =  str(file_obj['s3']['object']['key'])
         print("filename", filename)
         fileObj = s3.get_object(Bucket = "my-lambda-trigger-bucket",  Key=filename)
         file_content = fileObj["Body"].read().decode('utf-8')
         print(file_content)
    
   
    return 'S3 Lambda Trigger!'
    
