import os, io, boto3, json, csv
from io import BytesIO
import base64
from PIL.Image import core as _imaging
from PIL import Image
    

ENDPOINT_NAME = '' # enter your ENDPOINT_NAME 
runtime= boto3.client('sagemaker-runtime')

# helper decoder
def decode_base64_image(image_string):
  base64_image = base64.b64decode(image_string)
  buffer = BytesIO(base64_image)
  return Image.open(buffer)

def generate_images(prompt, num_images_per_prompt):
    data = {
        "inputs": prompt,
        "num_images_per_prompt" : num_images_per_prompt
    }
    
    payload = json.dumps(data, indent=2).encode('utf-8')
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=payload)
                                       
    print('response: ' + str(response))
    
    print('response body: ' + str(response['Body']))
    
    response_decoded = json.loads(response['Body'].read().decode())
    
    print("response decoded: " + str(response_decoded))
    decoded_images = [decode_base64_image(image) for image in response_decoded["generated_images"]]

    return decoded_images