# Importing Libraries
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS 

# Function to convert text to speech
def textToSpeech(text,fileName):
    pass

# Returns pydub audio segments
def mergeAudios(audios):
    pass

def generateSkeleton():
    audio = AudioSegment.from_mp3("audios/railway.mp3")
    #1- Alert Message
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format ="mp3") 
    
    #2 - from city


    #3 - starting station
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format ="mp3")

    #4 - via city

    #5 - passing city
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format ="mp3") 

    #6 - to city

    #7 - going through
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format ="mp3") 

    #8 - Train Name and Number


    #9 - Coming after some time
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format ="mp3") 


    #10 - Platform number


    #11 - Arrival Timing
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format ="mp3") 


def generateAnnouncement(fileName):
    pass 


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()

    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")

