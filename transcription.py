import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import whisper

model = whisper.load_model("base")
filepath = ""
filedest = ""

def openDestination():
    global filedest
    filedest = filedialog.askdirectory()
    print(filedest)

def openDirectory():
    global filepath
    filepath = filedialog.askopenfilename()
    templabel = ttk.Label(mainframe, text=filepath).grid(column=1, row=2, sticky=(N, S))
    return filepath

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']
def transcribe():
    global filepath
    print("This is the filepath: " + filepath)
    audio_path = filepath
    transcribed_text = transcribe_audio(audio_path)
    file = open(filedest + "/transcription.txt", "w")
    file.write(transcribed_text)


window = Tk()
window.title("Transcriptor")
mainframe = ttk.Frame(window, padding="20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

button = ttk.Button(mainframe, text="Choose directory", command=openDirectory)
label = ttk.Label(mainframe, text="Chose the directory of your audio file: ")
label.grid(column=1, row=1, sticky=(W))
button.grid(column=2, row=1, sticky=(N))

destination = ttk.Label(mainframe, text="Chose the transcription destination: ").grid(column=1, row=3, sticky=N)
destbutton = ttk.Button(mainframe, text="Destination", command=openDestination).grid(column=2, row=3, sticky=N)
transcribebutton = ttk.Button(mainframe, text="Transcribe", command=transcribe).grid(column=2, row=4, sticky=N)

window.mainloop()