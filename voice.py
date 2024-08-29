import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def main():
    """Main function for the voice assistant."""
    speak("Hello! How can I assist you today?")
    
    while True:
        text = listen().lower()
        if "exit" in text or "quit" in text:
            speak("Goodbye!")
            break
        elif "hello" in text:
            speak("Hello there!")
        elif "how are you" in text:
            speak("I'm an AI, so I'm always good. How about you?")
        else:
            speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    main()
