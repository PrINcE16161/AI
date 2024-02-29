import datetime
from turtle import color

import pyttsx3
import speech_recognition as sr
import subprocess   #create note

from selenium_web import *  #install chrome-driver
from YT_auto import *   #play youtube video
from News import *  #for news

import randfacts    #for facts

from jokes import *     #for jokes
from weather import *   #for weather

import tkinter as tk
from threading import Thread

today_date = datetime.datetime.now()

def create_gui():
    global label
    root = tk.Tk()
    root.geometry("200x200+1300+20")
    root.title("Voice Assistant")
    root.overrideredirect(True)
    label = tk.Label(root, text="🤖", font=("Arial", 150), fg="black")
    label.pack()

    root.mainloop()

def update_label(color):
    label.config(fg=color)

def speak(text,color='red'):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    update_label(color)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>6 and hour<=12:
        return("Good Morning.")
    elif hour>12 and hour<=18:
        return("Good Afternoon.")
    elif hour>18 and hour<=24:
        return("Good Evening.")
    else:
        return("Good Night.")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


gui_thread = Thread(target=create_gui)
gui_thread.start()

WAKE = "hey jenny"
EXIT = ["stop", "exit", "quit"]
print("Start")
speak("hello sir," + wishme() + " i'm your voice assistant, Jenny")
speak("Today is "+today_date.strftime("%d")+" of "+today_date.strftime("%B")+" And it's currently " +(today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
speak("Temperature in Vadodara is"+str(temp())+" degree celsius and with "+str(des()))
update_label(color='black')

while True:
    print("Listening")
    text = get_audio()

    if any(exit_command in text for exit_command in EXIT):
        speak("Goodbye, have a great day!")
        update_label(color='gray')
        gui_thread.join()
        break

    if text.count(WAKE) > 0:
        speak("I am ready")
        update_label(color='black')
        text = get_audio()

        NOTE_STRS = ["make a note", "write this down", "remember this","create a note","note"]
        for phrase in NOTE_STRS:
            if phrase in text:
                speak("What would you like me to write down?")
                note_text = get_audio()
                note(note_text)
                speak("I've made a note of that.")
                update_label(color='black')
                break

        INFORMATION = ["tell me some information", "information"]
        for phrase in INFORMATION:
            if phrase in text:
                speak("You need information related to which topic?")
                infor = get_audio()
                print("searching {} in wikipedia".format(infor))
                speak("searching {} in wikipedia".format(infor))
                assist = infow()
                assist.get_info(infor)
                update_label(color='black')
                break

        YOUTUBE = ["play video", "play", "song"]
        for phrase in YOUTUBE:
            if phrase in text:
                speak("you want me to play which video??")
                vid = get_audio()
                print("Playing {} on youtube".format(vid))
                speak("Playing {} on youtube".format(vid))
                assist = music()
                assist.play(vid)
                update_label(color='black')
                break

        NEWS = ["news"]
        for phrase in NEWS:
            if phrase in text:
                speak("Sure sir, Now I will read news for you.")
                arr = news()
                for i in range(len(arr)):
                    print(arr[i])
                    speak(arr[i])
                update_label(color='black')
                break

        FACT = ["tell me a fact", "fact", "facts"]
        for phrase in FACT:
            if phrase in text:
                speak("Sure sir,")
                x = randfacts.get_fact()
                print(x)
                speak("Did you know that," + x)
                update_label(color='black')
                break

        JOKE = ["tell me a joke", "funny", "joke", "jokes"]
        for phrase in JOKE:
            if phrase in text:
                speak("Sure sir, get ready for chuckles")
                ar = joke()
                print(ar[0])
                speak(ar[0])
                print(ar[1])
                speak(ar[1])
                update_label(color='black')
                break
