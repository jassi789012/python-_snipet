import speech_recognition as sr
import pyttsx3
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you repeat?")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error during speech recognition: {e}")
        return None

def open_application(application_name):
    try:
        subprocess.Popen([application_name], shell=True)
        speak(f"Opening {application_name}")
    except FileNotFoundError:
        print(f"Error: Application '{application_name}' not found.")
        speak(f"Sorry, I couldn't find the application {application_name}.")
    except Exception as e:
        print(f"Error opening application: {e}")
        speak("Sorry, I encountered an error while trying to open the application.")

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you today?")

    while True:
        command = listen()

        if command:
            if "open" in command:
                app_to_open = command.split("open", 1)[1].strip()
                open_application(app_to_open)
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that command. Can you please repeat?")
