import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1: generate kripya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3") 

    # 2: is from city

    #3: generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3") 

    # 4: via city
    
    #5: generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3") 

    #6: to city
    
    # 7: generate ko jaane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3") 

    #8: is train number and name
    
    #9: generate kuch hi samay mein platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3") 

    #10: platform number
    
    #11: generate par aa rhi h
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3") 
    
    # 1: generate may i have ur attention please
    start = 1530000
    finish = 156000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3") 

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2: is from city
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4: via city
        textToSpeech(item['via'], '4_hindi.mp3')
        #6: to city
        textToSpeech(item['to'], '6_hindi.mp3')
        #8: is train number and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        #10: platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton")
    generateSkeleton()
    print("Now generating Announcements...")
    generateAnnouncement("announce_hindi.xlsx")
