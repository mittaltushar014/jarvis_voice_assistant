import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("I am Jarvis sir! Please tell me How may I help you")
    speak("I am Jarvis sir! Please tell me How may I help you")

def takecommand():
    '''It takes microphone Input from User and returns String output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again please!")
        return "None"

    return query        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'password')
    server.sendmail('email@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    print("Welcome! Tushar Sir!")
    speak("Welcome! Tushar Sir!")
    wishme()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia:")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com') 

        elif 'open google' in query:
            webbrowser.open('www.google.com')  

        elif 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')      

        elif 'open code' in query:
            codepath='C:\\Users\\mitta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)      

        elif 'play music' in query:
            musicpath="E:\\music\\Relaxing"
            songs=os.listdir(musicpath)
            print(songs)
            os.startfile(os.path.join(musicpath,songs[1]))

        elif 'time' in query:
            timenow=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {timenow}")    

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tusharmittal1410@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email") 
    
        elif 'quit' in query:
            exit()
