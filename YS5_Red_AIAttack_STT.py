pip3 install SpeechRecognition pydub #Go to Command Prompt and install this line
pip3 install pyaudio #Go to Command Prompt and install this line

import speech_recognition as sr

speech_r = sr.Recognizer()

#Loading audio file and converting speech to text
with sr.Microphone() as source:
    print('Talking...')
    # read the audio data from the default microphone
    audio_data = speech_r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = speech_r.recognize_google(audio_data)
    print(text)
