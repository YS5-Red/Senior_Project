#pip3 install SpeechRecognition pydub
#pip3 install pyaudio

import speech_recognition as sr

speech_r = sr.Recognizer()

#Loading audio file and converting speech to text
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = speech_r.record(source, duration=10) #Taking in audio for 10secs
    print("Recognizing...")
    # convert speech to text
    text = speech_r.recognize_google(audio_data)
    print(text)
