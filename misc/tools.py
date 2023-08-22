#Fundamental Tools
import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    
##def takeCommand():
##    query = ""
##    r = sr.Recognizer()
##    with sr.Microphone() as source:
##        print("Listening........")
##        audio = r.listen(source)
##        query = r.recognize_google(voice)
##        return query

def takeCommand():
    query = ""
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        speak("Listening")
        audio = r.listen(source)
    try :
        speak("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please")
        takeCommand()
        
    return query

def features():
    speak("I can do")
