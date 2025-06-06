import pyttsx3
import speech_recognition as sr
from colorama import Fore, Style, init
import pyfiglet
import time

# Initializing colorama
init(autoreset=True)

# Display ASCII Logo
ascii_banner = pyfiglet.figlet_format("Voice Buddy 🎙️")
print(Fore.MAGENTA + ascii_banner)
time.sleep(1)
print(Fore.CYAN + "✨ Your Personal Voice Assistant is Ready! ✨\n")
time.sleep(0.5)

# Text to Speech Function
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

# Speech to Text Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.CYAN + "🎙️ Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(Fore.GREEN + "📝 You said: " + Style.BRIGHT + text)
        except sr.UnknownValueError:
            print(Fore.RED + "⚠️ Could not understand audio.")
        except sr.RequestError:
            print(Fore.RED + "⚠️ Could not request results, check your internet connection.")

# Speak After Me Function
def speak_after_me():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.CYAN + "🎙️ Say something, I'll repeat it back...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(Fore.GREEN + "📝 You said: " + Style.BRIGHT + text)
            text_to_speech(f"You said: {text}")
        except sr.UnknownValueError:
            print(Fore.RED + "⚠️ Could not understand audio.")
        except sr.RequestError:
            print(Fore.RED + "⚠️ Could not request results, check your internet connection.")

# Stylish Menu-driven app
while True:
    print(Fore.MAGENTA + "\n===== 🎙️ Voice Assistant Menu =====")
    print( "1. Text to Speech")
    print("2. Speech to Text")
    print("3. Speak After Me")
    print("4. Exit")

    choice = input(Fore.CYAN + "Enter your choice (1-4): ")

    if choice == '1':
        text = input(Fore.GREEN + "Enter text to speak: ")
        text_to_speech(text)

    elif choice == '2':
        speech_to_text()

    elif choice == '3':
        speak_after_me()

    elif choice == '4':
        print(Fore.YELLOW + "👋 Exiting... See you soon, buddy!")
        break

    else:
        print(Fore.RED + "⚠️ Invalid choice. Please select 1-4.")
