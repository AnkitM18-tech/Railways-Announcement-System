# Importing Libraries
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS 

# Function to convert text to speech
def textToSpeech(text,fileName):
    myText = str(text)
    language = 'hi'
    myObj = gTTS(text = myText, lang = language, slow = False)
    myObj.save(fileName)

# Returns pydub audio segments
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)

    return combined

#Generate Skeleton for Announcement
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

#Generate Announcement
def generateAnnouncement(fileName):
    df = pd.read_excel(fileName)
    for index, item in df.iterrows():

        # 2 - Generate from-city
        textToSpeech(item["from"], "2_hindi.mp3")

        # 4 - Generate via-city
        textToSpeech(item["via"], "4_hindi.mp3")

        # 6 - Generate to-city
        textToSpeech(item["to"], "6_hindi.mp3")

        # 8 - Generate train no and name
        textToSpeech(item["train_no"] + " " + item["train_name"], "8_hindi.mp3")

        # 10 - Generate platform number
        textToSpeech(item["platform"], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format= "mp3")

#Driver function
if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()

    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")