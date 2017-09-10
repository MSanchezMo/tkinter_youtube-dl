from tkinter import Tk, Button, Entry, StringVar, Label, Text, END
from files.classes.logger import Logger
import os
import youtube_dl
import time


download_dir = '/home/c4nt30/Vídeos/test' 
window = Tk()
t1 = Text(window, height=1, width=60)


def printInField(text, t1):
    t1.delete(1.0, END)
    t1.insert(1.0, text)
    

def hook(d, t1=t1):
    """_eta_str
    total_bytes
    eta
    filename
    _total_bytes_str
    speed
    downloaded_bytes
    elapsed
    status
    _speed_str
    tmpfilename
    _percent_str"""
    
    if d['status'] == 'finished':
        printInField('OK', t1)
    elif d['status'] == 'downloading':
        printInField(d['_percent_str'], t1)
        
        
def download(ydl_opts, url_value):
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_value.get()])



def initialize_window(ydl_opts, download_dir, t1):
    

    l1_value = StringVar()
    l1 = Label(window, textvariable=l1_value)
    l1_value.set(download_dir)
    
    url_value = StringVar()
    url = Entry(window, textvariable=url_value)
    
    
    
    
    b1 = Button(window, text="Download", command=lambda: download(ydl_opts, url_value))
    
    l1.grid(row=0, column=0)
    url.grid(row=0, column=1)
    b1.grid(row=0, column=2)
    t1.grid(row=1, columnspan=3)
    
    window.mainloop()
            
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'writedescription' : '.description',
    'logger': Logger(),
    'progress_hooks': [hook],
    
    'outtmpl':'%(title)s.%(ext)s'
}

os.chdir(download_dir)
initialize_window(ydl_opts, download_dir, t1)



    
