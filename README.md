# Speech-to-Text
Text to image in artificial intelligence is the generation of images based on a given prompt. It requires a prominent level of natural language processing and image generation. Text deciphering to generate images is a major field in AI and still a work in progress as real image collection and processing is expensive.


![image](https://user-images.githubusercontent.com/89687363/202844735-23ceab34-e672-43b6-982c-1289b0dd8ba5.png)


Once an mp3 recording is uploaded into the S3 a lambda function will call Amazon Transcribe to transcribe the recording (speech-to-text), then it will call Amazon Translate to translate the transcribed text (text-to-text), and finally, it will invoke the HuggingFace model deployed on SageMaker to generate an image from the translated text (text-to-image) that is also uploaded to the specific sub-bucket.
