import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')  # Initialize TTS engine
    voices = engine.getProperty('voices')  # Get available voices
    #print("Available voices:", voices)  # Debugging: List voices
    
    engine.setProperty('voice', voices[0].id)  # Select voice (e.g., 1 for female voice)
    engine.setProperty('rate', 174)  # Set speed of speech
    
    eel.DisplayMessage(text)  # callin to display in our food display
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Speak the queued text


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        recognizer.pause_threshold = 1  # Adjust silence threshold
        recognizer.adjust_for_ambient_noise(source)  # Calibrate to ambient noise
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)  # Capture audio, phrase_time_limit lee chai within 60 second vitra ko kura listin gar x yo vand dheari gardai na,and  timeout le system o va ko 10 secconbhitra bole na vane off hu xa
            print("Recognizing...") 
            eel.DisplayMessage("Recognizing...")#used to display in frontend by calling displaymessag() from conrtol.js
            query = recognizer.recognize_google(audio, language='en-in')  # Use Google recognizer
            print(f"User said: {query}")  # Print the recognized text
            eel.DisplayMessage(query)#used to display in frontend by calling displaymessag() from conrtol.js
            time.sleep(2)
            #speak(query)
            
            return query.lower()  # Return in lowercase for consistency
            
            
        except sr.WaitTimeoutError:
            print("Timeout! No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

@eel.expose
def all_command():
    query = take_command()
    print(query)

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)#function calling
    elif"on youtube":
        from engine.features import PlayYoutub #import palyoutube
        PlayYoutub(query)
    else:
        print('not run')  
    eel.ShowHood() #callig fun that go back to home page      



