import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Record audio for up to 5 seconds

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the request to Google Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech()
