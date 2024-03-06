import requests
import json
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....") r.energy_threshold = 300
        audio = r.listen(source,0,4)

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey='ENTER YOUR API KEY'",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey='ENTER YOUR API KEY'",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey='ENTER YOUR API KEY'",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey='ENTER YOUR API KEY'",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey='ENTER YOUR API KEY'",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey='ENTER YOUR API KEY'"
    }

    while True:
        content = None
        url = None
        speak("Which field news do you want to listen")
        print("[business]  [health]  [technology] [sports]  [entertainment]  [science]")
        field = input("Enter the name here :")
        for key, value in api_dict.items():
            if key.lower() in field.lower():
                url = value
                print(url)
                print("url was found")
                break
            else:
                url = True
        if url is True:
            print("url not found")
            continue 
        

        news = requests.get(url).text
        news = json.loads(news)
        speak("Here is the first news.")

        arts = news["articles"]
        for articles in arts:
            article = articles["title"]
            print(article)
            speak(article)
            news_url = articles["url"]
            print(f"for more info visit: {news_url}")

            a = input("[press 1 to continue] and [press 2 to stop]")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                speak("That's all")
                return 

