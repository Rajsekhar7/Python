import pyttsx3
import datetime
import speech_recognition as sr

engine= pyttsx3.init('sapi5') #speech api
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)#given the audio input
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak(' master Raj! How can I help you')

def takeCommand():
    #takes input from microphone and provide output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1 #increases the time of hearing to 1 sec
        r.energy_threshold=100
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        #using the Google Cloud Speech-to-Text API to recognize speech from an audio file
        print(f"Raj: {query}\n")
    except Exception as e:
        print(f"Alfred: {e}\n")
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    takeCommand()