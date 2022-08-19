#LANGUAGE_TRANSLATOR
import speech_recognition as spr
from itranslate import itranslate as itrans
from gtts import gTTS
import os
import pyaudio

recog1 = spr.Recognizer()
mc = spr.Microphone()
from_lang = 'en'
to_lang = 'hi'
while(True):
    with mc as source:  
        print("Speak a stentence...")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        get_sentence = recog1.recognize_google(audio)
        print(get_sentence)
        try:
            # print("Phase to be Translated :"+ get_sentence)
            text = itrans(get_sentence, to_lang="ta")
            print(text)
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("captured_voice.mp3")    
            os.system("start captured_voice.mp3")
        except spr.UnknownValueError:
            print("Unable to Understand the Input")        
        except spr.RequestError as e:
            print("Unable to provide Required Output", e)
    break       
