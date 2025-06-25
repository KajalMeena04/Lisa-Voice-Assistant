"""
Lisa  Your Personal Voice Assistant

Lisa is a Python-based voice assistant that can perform tasks like:
- Playing songs
- Opening websites
- Reading the latest news
- Answering general questions using AI


How to Set It Up:
1. Make sure you have Python 3.8 or higher installed.
2. Open a terminal or command prompt and install the required libraries:

   pip install speechrecognition pyttsx3 pygame requests google-generativeai gTTS pywhatkit

3. If you're running the program for the first time, ensure your system has microphone access enabled.
4. Create a news api key .
5. Run the program using:

   python main.py


How to Use Lisa:
- Say "Lisa" to activate the assistant (this is the wake word).
- After activation, speak your command clearly.(It show it's activation by saying 'yaa')
- Note: You must say "Lisa" every time before giving a command.


Examples of Commands:
- "Lisa, play Shape of You"
- "Lisa, open YouTube"
- "Lisa, tell me the news"
- "Lisa, what is the capital of France?"
- "Lisa, shut up" (to stop the assistant)


How It Works:
- Lisa uses Google Gemini API to handle general queries.
- It plays songs from YouTube using pywhatkit.
- News is fetched from NewsAPI based on the current date.
- Voice responses are generated using Google Text-to-Speech (gTTS) and played using pygame.
- A temporary audio file is created and deleted automatically during playback.

"""

