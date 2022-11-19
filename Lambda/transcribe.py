import json, boto3
from urllib.request import urlopen
import time


transcribe = boto3.client('transcribe')

def transcribe_mp3(file_name, object_url):
    try:
        response = transcribe.delete_transcription_job(
            TranscriptionJobName='audio-rawV')
    except:
        print('Transcription job name does not exist.')
    response = transcribe.start_transcription_job(
        TranscriptionJobName=file_name.replace('/','')[:10],
        LanguageCode='ar-AE', # source Language
        MediaFormat='mp3',
        Media={
            'MediaFileUri': object_url
        })
    while True :
        status = transcribe.get_transcription_job(TranscriptionJobName='audio-rawV')
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED','FAILED']:
            break
        print('In Progress')
        time.sleep(5)
    load_url = urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
    load_json = json.dumps(json.load(load_url))
    text = str(json.loads(load_json)['results']['transcripts'][0]['transcript'])
    
    return text