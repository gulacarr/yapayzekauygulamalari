import speech_recognition as sr
import webbrowser as webbrowser
import datetime as datetime
import time

from gtts import gTTS
from playsound import playsound
import random
import os

r=sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice=''
        
        try:
            voice=r.recognize_google(audio,language="tr-TR")
            
        except sr.UnknownValueError:
            speak('cano ne söylediğini anlayamadım.')
            
        except sr.RequestError:
            speak('bir hata oluştu.')
            
        return voice


def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim sen nasılsın')
    if 'havalar nasıl' in voice:
        speak('buralar yağmurlu oralar nasıl')
    if 'burası da yağmurlu' in voice:
        speak('şemsiyeni almayı unutma ıslanırsın')
    if 'görüşürüz' in voice:
        speak('görüşürüz cano')
    if 'arama yap' in voice:
        search=speak('senin için ne aramamı istersin.')
        url="https://google.com/search?q"+search
        webbrowser.get().open(url)
        speak(search +"ile ilgili bulduklarım")
        



def speak(string):
    tts=gTTS(string,lang="tr")
    rand=random.randint(1, 10000)
    file="audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
            
speak("merhaba nasılsın")    
time.sleep(1)
while 1:
    voice=record()
    print(voice)
    response(speak)
    