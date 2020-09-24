from gtts import gTTS
from playsound import playsound

def speak(text):
    tts = gTTS(text)
    tts.save('voice.mp3')
    playsound('voice.mp3')