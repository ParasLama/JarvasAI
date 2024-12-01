from playsound import playsound
import eel #this is used for linking frontend with banckend and vise versa

@eel.expose #which is used make able to link with js
#Playin Assintant sound function
def playAssistantSound():
    #you have to give double back slase
    music_dir="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
