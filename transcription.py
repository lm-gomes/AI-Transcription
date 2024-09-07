import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
    templabel = tkinter.Label(window, text=filepath).grid(column=1, row=2, sticky=(N, S))
    return filepath

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']
def transcribe_text():
    global filepath
    print("This is the filepath: " + filepath)
    audio_path = filepath
    transcribed_text = transcribe_audio(audio_path)
    file = open(filedest + "/transcription.txt", "w")
    file.write(transcribed_text)
    messagebox.showinfo("Success!",message="Transcription succeeded!")



window = Tk()
window.title("Transcriptor")
window.configure(bg="#273746", padx="20", pady="20")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

dirFrame = tkinter.Frame()
label = tkinter.Label(window, text="AI Transcription Tool", font=("Arial, 25"), bg="#273746", fg="white")
button = tkinter.Button(dirFrame, text="Choose directory", padx="20", font=("Arial, 8"), bg="#273746", fg="white", command=openDirectory)
dir_text = tkinter.Label(dirFrame, text="Chose the directory of your audio file: ", font=("Arial, 8"), bg="#273746", fg="white")
dirFrame.configure(background="#273746", padx="10", pady="10", highlightthickness="5", highlightbackground="white")

destination = tkinter.Label(window, text="Chose the transcription destination: ", font=("Arial, 8"), bg="#273746", fg="white")
destbutton = tkinter.Button(window, text="Destination", font=("Arial, 8"), bg="#273746", fg="white", padx="20")
transcribetext_button = tkinter.Button(window, text="Transcribe to Text", font=("Arial, 8"), bg="#273746", fg="white", command=transcribe_text)

#Grid manipulation
label.grid(column=1, row=1, rowspan=2)
dirFrame.grid(column=1, row=3)
dir_text.grid(column=1, row=3, padx=5)
button.grid(column=2, row=3, padx=5)
destination.grid(column=1, row=5)
destbutton.grid(column=2, row=5)
transcribetext_button.grid(column=1, row=6)
window.mainloop()