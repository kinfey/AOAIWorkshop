import os
import azure.cognitiveservices.speech as speechsdk
from openai import AzureOpenAI

client = AzureOpenAI(
azure_endpoint='Your Azure AI Service EndPoint',
api_key='Your Azure AI Service API Key',
api_version="2023-12-01-preview"
)

deployment_id='GPT4Model'

speech_config = speechsdk.SpeechConfig(subscription='Your Azure Speech Service API Key', region='Your Azure Speech Service Region')
audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

speech_config.speech_recognition_language="zh-CN"
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

speech_config.speech_synthesis_voice_name='zh-CN-YunxiNeural'
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)
tts_sentence_end = [ ".", "!", "?", ";", "。", "！", "？", "；", "\n" ]

def ask_openai(prompt):
    response = client.chat.completions.create(model=deployment_id, max_tokens=200, stream=True, messages=[
        {"role": "user", "content": prompt}
    ])
    collected_messages = []
    last_tts_request = None

    for chunk in response:
        if len(chunk.choices) > 0:
            chunk_message = chunk.choices[0].delta.content  
            if chunk_message is not None:
                collected_messages.append(chunk_message)  
                if chunk_message in tts_sentence_end: 
                    text = ''.join(collected_messages).strip() 
                    if text != '': 
                        print(f"Speech synthesized to speaker for: {text}")
                        last_tts_request = speech_synthesizer.speak_text_async(text)
                        collected_messages.clear()
    if last_tts_request:
        last_tts_request.get()

def chat_with_open_ai():
    while True:
        print("Azure OpenAI is listening. Say 'Stop' or press Ctrl-Z to end the conversation.")
        try:
            speech_recognition_result = speech_recognizer.recognize_once_async().get()

            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                if speech_recognition_result.text == "Stop.": 
                    print("Conversation ended.")
                    break
                print("Recognized speech: {}".format(speech_recognition_result.text))
                ask_openai(speech_recognition_result.text)
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
                break
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
        except EOFError:
            break

# Main

try:
    chat_with_open_ai()
except Exception as err:
    print("Encountered exception. {}".format(err))