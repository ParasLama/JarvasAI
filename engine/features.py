import os
import re #import regular expressino for youtube 
from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
import eel #this is used for linking frontend with banckend and vise versa
import pywhatkit as kit #it is liberary usred for youtube runn
@eel.expose #which is used make able to link with js
#Playin Assintant sound function
def playAssistantSound():
    #you have to give double back slase
    music_dir="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open","")
    query.lower()

    if query !="":
        speak("Opening"+query) # here speak is function we calling it 
        os.system('start'+query)
    else:
        speak("not found")    

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


