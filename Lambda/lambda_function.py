import json
import boto3
from transcribe import transcribe_mp3
from translate import translate_text
from hf_model import generate_images

from upload2s3 import upload_file

client = boto3.client ( 's3' )

#Create low level clients for s3 and Transcribe
# s3  = boto3.client('s3')

def lambda_handler(event, context):
    #parse out the bucket & file name from the event handler
    for record in event['Records']:
        file_bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        object_url = 'https://s3.amazonaws.com/{0}/{1}'.format(file_bucket, file_name)
        
        transcribed_text = transcribe_mp3(file_name, object_url)
        translated_text = translate_text(transcribed_text)
        generated_images = generate_images(translated_text, 2)

        for i, img in enumerate(generated_images):
            img_name = f'{translated_text.replace(" ", "_").replace(".","")}-{i}.jpeg'
            img_path = "/tmp/" + img_name
            img.save(img_path)
            upload_file(
                file_name=img_path,
                bucket='', # enter the s3 bucket name
                object_name='result/' + img_name
                )

            return "lambda handled Successfully!"
