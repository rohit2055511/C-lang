# ---------------------------------------------
#   VOICE COMMAND BASED VIRTUAL ASSISTANT
# ---------------------------------------------

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the engine (text-to-speech)
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listen to user voice and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except:
        speak("Sorry, please say that again.")
        return "None"
    return query.lower()

# Greeting message
speak("Hello! I am your virtual assistant. How can I help you today?")

while True:
    command = takeCommand()

    # 1. Time
    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    # 2. Date
    elif "date" in command:
        date = datetime.date.today()
        speak(f"Today's date is {date}")

    # 3. Google Search
    elif "search" in command or "google" in command:
        speak("What should I search?")
        query = takeCommand()
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)

    # 4. Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # 5. Open Notepad
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # 6. Exit
    elif "exit" in command or "stop" in command:
        speak("goodbye have a great day")
        break
