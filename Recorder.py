#arti's Voice recorder
#Import necessary modules
#from turtle import bgcolor
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
       

        

#Fit data into queue
def callback(indata, frames, time, status):
   q.put(indata.copy())
#Recording function




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



def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    t=playsound(filename)

        

voice_rec = Tk()
voice_rec.geometry("360x200")
voice_rec.title("Aarti's Voice Recorder")
voice_rec.config(bg="#800080")
#Create a queue to contain the audio data
q = queue.Queue()
#Declare variables and initialise them
recording = False#107dc2
file_exists = False
#Label to display app title in Python Voice Recorder Project
title_lbl  = Label(voice_rec, text="Aarti's Voice Recorder", bg="#107dc2").grid(row=0, column=0, columnspan=3)
 
#Button to record audio
record_btn = Button(voice_rec, text="Record Audio", bg='#FF7F7F',command=lambda m=1:threading_rec(m))
#Stop button
stop_btn = Button(voice_rec, text="Stop Recording", bg='#FFB6C1',command=lambda m=2:threading_rec(m))
#Play button
#play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3:threading_rec(m))
#Position buttons
record_btn.grid(row=1,column=1)
stop_btn.grid(row=1,column=0)
#open_button.grid(row=1,column=2)


open_button = Button(
    voice_rec,
    text="play(Open a File)",
    command=select_file ,bg='#FFB6C1'
    
)
#open_button.pack(expand=True)
open_button.grid(row=1,column=2)

voice_rec.mainloop()