
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Lisa. Please tell me how may I help you?")



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    '''
    It Takes Microphone input from the user and returns string as output
    '''
    r=sr.Recognizer() #Recognizer is a class
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia........")
            query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia.....")
            speak(results)
        elif "who are you" in query:
            speak("I am your virtual assistant and My Name is Lisa..")
        elif "how are you" in query:
            speak("I'm fine")
        elif "good morning" in query:
            speak(query)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open geeks for geeks" in query:
            webbrowser.open("geeksforgeeks.org")
        elif "play music" in query:
            music=r"D:\\Interview\\Python Personal Assistant\\Music.mp3"
            os.startfile(music)
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "open code" in query:
            codePath=r"C:\\Users\\Ravina\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        else:
            speak("Sorry, I didn't get you.... could you please repeat......")


        

        
            

    
