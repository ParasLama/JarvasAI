import os
import re
import webbrowser #import regular expressino for youtube 
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import eel #this is used for linking frontend with banckend and vise versa
import pywhatkit as kit #it is liberary usred for youtube runn

import sqlite3 
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose #which is used make able to link with js
#Playin Assintant sound function

def playAssistantSound():
    #you have to give double back slase
    music_dir="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").lower()
    
    # Fetching data from SQLite
    app_name = query.strip()
    if app_name:
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if results:
                speak(f"Opening {query}")
                os.startfile(results[0][0])

            else:
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                if results:
                    speak(f"Opening {query}")
                    webbrowser.open(results[0][0])

                else:
                    speak(f"Attempting to open {query}")
                    try:
                        os.system(f'start {query}')
                    except OSError as e:
                        speak("Command not found")
                        print(f"OS error: {e}")
        
        except sqlite3.Error as db_error:
            speak("Database error occurred.")
            print(f"Database error: {db_error}")
        
        except Exception as e:
            speak("An unexpected error occurred.")
            print(f"Unexpected error: {e}")


    

def PlayYoutub(query):
    search_term =extract_yt_term(query)
    speak("Playing"+search_term+"on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    #define a regular expressino pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #use re.serch to find the cmatch in the command 
    match = re.search(pattern,command,re.IGNORECASE)
    #if  amatch is found , ruturn the extracted song name; otherwise ,return none 
    return match.group(1) if match else None


