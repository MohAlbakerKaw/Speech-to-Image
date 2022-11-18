import boto3, json

translate = boto3.client ('translate')

def translate_text(text):
    result = translate.translate_text(
        Text = text,
        SourceLanguageCode = "auto",
        TargetLanguageCode = "en")
        
    prompt = result["TranslatedText"]
    
    return prompt
