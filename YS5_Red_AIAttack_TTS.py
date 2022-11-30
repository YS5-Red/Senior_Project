!pip install gTTS #Install this line in Command Prompt

from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class

#language to use
language = "en"

#random variable
num = input("Please enter a number 0, 1, 2: ")

#Choice of speech depending on number
if num == "0":
  speech = "Welcome to XYZ bank, please say your account number and pin."
elif num == "1":
  speech = "Welcome to XYZ internet, please say your account number and pin"
elif num == "2":
  speech = "Welcome to XYZ mobile, please say your account number and pin"
else:
  speech = "Invalid account number and/or pin"

#Provide the string to convert to speech
tts1 = gTTS(text = speech, lang = language, slow =False) 
tts1.save('1.wav') #save the string converted to speech as a .wav file
sound_file = '1.wav'
Audio(sound_file, autoplay=False) 
#Autoplay = True will play the sound automatically
#If you would not like to play the sound automatically, pass Autoplay = False.