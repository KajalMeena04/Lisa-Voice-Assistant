'''Read README file to know how to operate'''
# Do not forget to create api key for news
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
import pygame
import pywhatkit
from gtts import gTTS
from datetime import date



recognizer=sr.Recognizer() 
engine=pyttsx3.init() 
# paste api key in the quotes 
newsapi=""

def play_youtube_song(song_name):
    pywhatkit.playonyt(song_name)

def speak(text):
    tts=gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    
def aiProcess(command):
    genai.configure(api_key="AIzaSyAj-ehLHpkGRDDFhdocSnf3GlT_39i26xg")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(command)
    return response.text
  
def processCommand(c):
    c = c.lower()

    if "open" in c:
        words = c.split()

        # Some sites for frequent use added here in case of  fallback of voice
        special_sites = {
            "google": "https://www.google.com",
            "facebook": "https://www.facebook.com",
            "youtube": "https://www.youtube.com",
            "linkedin": "https://www.linkedin.com",
            "instagram": "https://www.instagram.com",
            "leetcode": "https://leetcode.com",
            "gfg": "https://www.geeksforgeeks.org",
            "geeksforgeeks": "https://www.geeksforgeeks.org",
            "codeforces": "https://codeforces.com",
            "code": "https://codeforces.com",
            "forces": "https://codeforces.com",
            "codingninjas": "https://www.codingninjas.com",
            "codechef": "https://www.codechef.com",
            "hackerrank": "https://www.hackerrank.com"
        }

        try:
            site_index = words.index("open") + 1
            site_name = words[site_index]

            if site_name in special_sites:
                url = special_sites[site_name]
            elif site_index + 1 < len(words) and f"{site_name} {words[site_index + 1]}" in special_sites:
                url = special_sites[f"{site_name} {words[site_index + 1]}"]
            else:
                cleaned_name = site_name.replace(".", "").lower()
                url = f"https://www.{cleaned_name}.com"

            speak(f"Opening {site_name}")
            webbrowser.open(url)
            return
        except (IndexError, ValueError):
            speak("Sorry, I didn't catch the website name.")
            return
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        speak(f"Playing {song} from YouTube")
        play_youtube_song(song)

    
    elif "news" in c.lower():
        today = date.today()
        date_str = today.isoformat()
        url = f"https://newsapi.org/v2/everything?q=apple&from={date_str}&to={date_str}&sortBy=popularity&apiKey={newsapi}"
        r = requests.get(url)
        data = r.json()

        # Check if the request was successful
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            speak("Here are the top news headlines.")
            for i, article in enumerate(articles[:5]):
                title = article.get("title", "No Title Available")
                print(f"{i+1}. {title}")
                speak(title)
        else:
            print("Error fetching data:", data.get("message", "Unknown error"))
    elif "shut up" in c.lower():
        speak("Okay sorry")  
      
    else:
        # OpenAI here handle the request
        output=aiProcess(c)
        speak(output)
    
 
    
if __name__=="__main__":
    speak("Initializing Lisa....")
    while True:
        # Listen for the wake word "Lisa"
        # Obtain audio from the microphone
        
        print("recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio= recognizer.listen(source,timeout=5,phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            print(word)
            if (word.lower()=="lisa"):
                speak("Yaa ")
                # Listen for command
                with sr.Microphone() as source:
                    print("Lisa Active...")
                    audio= recognizer.listen(source)
                    command=recognizer.recognize_google(audio)
                    print(command)
                    processCommand(command)
                    
                    
        except Exception as e:
            print("Error; {0}".format(e))
            speak("Sorry, can you repeat that? I was unable to recognize.")
