import pyttsx3

def generate_shoutout(name):
    return f"Shoutout to {name.upper()}!"

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def main():
    # Replace this list with your own list of names
    names = ["jaswinder singh", "parveen kumari", "balwant singh"]

    # Generate shoutouts for each name
    shoutouts = [generate_shoutout(name) for name in names]

    # Convert shoutouts to speech and listen
    for shoutout in shoutouts:
        print(shoutout)
        text_to_speech(shoutout)

if __name__ == "__main__":
    main()
