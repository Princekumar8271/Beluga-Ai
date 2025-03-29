import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from train_ai import AIModel

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# Select first available female voice (index 1 is typically female)
if len(voices) > 2:  # If there are multiple female voices available
    engine.setProperty("voice", voices[2].id)  # Try using another female voice
else:
    engine.setProperty("voice", voices[1].id)  # Fallback to default female voice
engine.setProperty("rate", 150)  # Slower speech rate
engine.setProperty("pitch", 110)  # Slightly higher pitch
engine.setProperty("volume", 0.9)  # Slightly lower volume

def speak(audio):
    print(f"SPEAK: {audio}")  # Debug statement
    
    # Import numpy if not already imported
    import numpy as np
    
    # Add natural pauses between sentences
    sentences = [s.strip() for s in audio.split('.') if s.strip()]
    
    # Configure more natural speech parameters
    base_rate = 150
    base_pitch = 110
    
    for sentence in sentences:
        # Add slight variations to make speech more natural
        rate_variation = np.random.randint(-15, 15)
        pitch_variation = np.random.randint(-8, 8)
        
        engine.setProperty("rate", base_rate + rate_variation)
        engine.setProperty("pitch", base_pitch + pitch_variation)
        engine.setProperty("volume", 0.85 + np.random.uniform(-0.05, 0.05))
        
        # Add slight pause before speaking
        engine.runAndWait()
        engine.say(sentence)
        engine.runAndWait()  # Subtle pitch changes

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 21:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am Beluga. Please tell me how can I help you today.")

def takeCommand(retries=5):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("I didn't catch that. Could you please repeat?")
        if retries > 0:
            return takeCommand(retries - 1)
        else:
            return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("I am having trouble connecting to the service. Please check your internet connection.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        speak("Something went wrong. Please try again.")
        return "None"
    return query

if __name__ == "__main__":
    # Initialize AI model
    ai_model = AIModel()
    if not ai_model.load_model():
        print("AI model not found. Please train the model first by running train_ai.py")
        speak("I need to be trained first. Please run the training program.")
        exit()
        
    wishMe()
    while True:
        query = takeCommand().lower()

        if query == "none":
            continue

        # Use AI model to predict command
        predicted_command = ai_model.predict(query)
        
        if predicted_command == "stop_program":
            speak("Stopping the program.")
            print("Stopping the program.")
            break

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            except Exception as e:
                print(f"Error fetching Wikipedia results: {e}")
                speak("I couldn't fetch the information. Please try again.")
        
        elif 'open youtube' in query:
            speak("Opening YouTube in your default browser...")
            webbrowser.open("youtube.com")
            speak("YouTube is now ready for you!")
        
        elif 'open google' in query:
            speak("Launching Google for you...")
            webbrowser.open("google.com")
            speak("Google is now open in your browser.")

        elif 'open stack overflow' in query:
            speak("Accessing Stack Overflow...")
            webbrowser.open("stackoverflow.com")
            speak("Stack Overflow is ready for your coding questions!")
        
        elif 'open github' in query:
            speak("Opening GitHub...")
            webbrowser.open("github.com")
            speak("GitHub is now open. Happy coding!")
        
        elif 'open linkedin' in query:
            speak("Connecting you to LinkedIn...")
            webbrowser.open("linkedin.com")
            speak("LinkedIn is now open for networking.")

        elif 'open spotify' in query:
            speak("Starting Spotify for you...")
            os.system("spotify")
            speak("Spotify is now playing your favorite tunes!")
        
        elif 'open facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
            speak("Facebook is now ready for socializing!")

        elif 'open instagram' in query:
            speak("Launching Instagram...")
            webbrowser.open("instagram.com")
            speak("Instagram is now open. Enjoy your scrolling!")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ASUS\\Music\\New folder'
            if not os.path.exists(music_dir):
                speak("Music directory does not exist.")
                continue

            songs = os.listdir(music_dir)
            if not songs:
                speak("No songs found in the music directory.")
                continue

            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak(f"Playing {songs[0]}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")