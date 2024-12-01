import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')  # Initialize TTS engine
    voices = engine.getProperty('voices')  # Get available voices
    print("Available voices:", voices)  # Debugging: List voices
    
    engine.setProperty('voice', voices[0].id)  # Select voice (e.g., 1 for female voice)
    engine.setProperty('rate', 174)  # Set speed of speech
    
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Speak the queued text

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Adjust silence threshold
        recognizer.adjust_for_ambient_noise(source)  # Calibrate to ambient noise
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)  # Capture audio, phrase_time_limit lee chai within 60 second vitra ko kura listin gar x yo vand dheari gardai na,and  timeout le system o va ko 10 secconbhitra bole na vane off hu xa
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')  # Use Google recognizer
            print(f"User said: {query}")  # Print the recognized text
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

# Main logic
text = take_command()  # Capture user speech
if text:  # If speech is recognized
    speak(text)  # Speak it back
else:
    speak("Sorry, I didn't catch that. Please try again.")