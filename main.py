import sqlite3
import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
import datetime 
from tkinter import ttk
from tkinter import filedialog as fd
from playsound import playsound
import assemblyai as aai
import os
import API_key
import time
def create_folder(name):
    if not os.path.exists(name):
        os.mkdir(name)


if __name__ == "__main__":
    name = "Outputs"
    create_folder(name)


#Functions to play, stop and record audio in Python voice recorder
#The recording is done as a thread to prevent it being the main process
def threading_rec(x):
   if x == 1:
       #If recording is selected, then the thread is activated
       t1=threading.Thread(target= record_audio)
       t1.start()
   elif x == 2:
       #To stop, set the flag to false
       global recording
       recording = False
       messagebox.showinfo(message="Recording finished")
   elif x == 3:
       #To play a recording, it must exist.
       t2=threading.Thread(target=select_file.t)

   elif x == 4:
       #To play a recording, it must exist.
       t2=threading.Thread(target= convert)
       

        

#Fit data into queue
def callback(indata, frames, time, status):
   q.put(indata.copy())
#Recording function

def create_database():
    conn = sqlite3.connect('Outputs/credentials.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (
                        id INTEGER PRIMARY KEY,
                        datetime TEXT,
                        file TEXT,
                        text TEXT
                    )''')
    conn.commit()
    conn.close()


def record_audio():
   #Declare global variables   
   global recording
   #Set to True to record
   recording= True  
   global file_exists
   #Create a file to save the audio
   messagebox.showinfo(message="Recording Audio. Speak into the mic")
   dt=datetime.datetime.now().strftime('%d %m %y  %H_%M_%S_ %p')
   with sf.SoundFile(dt+".wav", mode='w', samplerate=44100,
                       channels=2) as file:
   #Create an input stream to record audio without a preset time
           with sd.InputStream(samplerate=44100, channels=2, callback=callback):
               while recording == True:
                   #Set the variable to True to allow playing the audio later
                   file_exists =True
                   #write into file
                   file.write(q.get())
#Define the user interface for Voice Recorder using Python
   

######################################################################################
def convert():
    create_database()
   
    # file=record_audio.dt
    #get api key from another file API_key.py
    aai.settings.api_key = API_key.API_KEY
    transcriber = aai.Transcriber()
    dt=datetime.datetime.now().strftime('%d %m %y  %H_%M_%S_ %p')
    filetypes = (
        ('media files', '*.mp3'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
            title='Open a file',
            initialdir='Outputs',
            filetypes=filetypes)

    transcript = transcriber.transcribe(filename)
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    conn = sqlite3.connect('Outputs/credentials.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO credentials (datetime, file, text) VALUES (?, ?, ?)", (dt, filename, transcript.text))
    conn.commit()
    conn.close()
    # start_time = time.time()
    # end_time = time.time()
    # execution_time = end_time - start_time*1000
    # # print("Execution time:", execution_time, "seconds")
    

    print(dt)
    print(transcript.text)
    # # print("Execution time:", '{:.2f}'.format(execution_time), "seconds")
    # print("Execution time:", '{:.2f}'.format(execution_time), "milliseconds")
#######################################################################################
def measure_execution_time():
    start_time = time.time()
    convert()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='Outputs',
        filetypes=filetypes)
    
    t=playsound(filename)

        

voice_rec = Tk()
voice_rec.geometry("250x95")
voice_rec.title("podRecord")
voice_rec.config(bg="#fff2cc")
#Create a queue to contain the audio data
q = queue.Queue()
#Declare variables and initialise them
recording = False#107dc2
file_exists = False
#Label to display app title in Python Voice Recorder Project
title_lbl  = Label(voice_rec, text=" Voice Recorder", bg="#d4f7c7").grid(row=0, column=0, columnspan=3)

#Button to record audio
record_btn = Button(voice_rec, text="Record Audio", bg='#FFB6C1',command=lambda m=1:threading_rec(m))
#Stop button
stop_btn = Button(voice_rec, text="Stop Recording", bg='#FFB6C1',command=lambda m=2:threading_rec(m))
#Play button
#play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3:threading_rec(m))
# convert_btn = Button(voice_rec, text="ToText", bg='#FF7F7F', command= lambda m=4: threading_rec(m))
#Position buttons
record_btn.grid(row=1,column=2)
stop_btn.grid(row=1,column=1)
# open_button.grid(row=2,column=1)
# convert_btn.grid(row=2 , column=1)

convert_button = Button(
    voice_rec,
    text="AUD_ToText",
    command=convert ,bg='#FFB6C1'
    
)

open_button = Button(
    voice_rec,
    text="play(Open File)",
    command=select_file ,bg='#FFB6C1'
    
)
#open_button.pack(expand=True)
open_button.grid(row=3,column=1)
convert_button.grid(row=3, column=2)
voice_rec.mainloop()
