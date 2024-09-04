import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import whisper
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


model = whisper.load_model("base")
filepath = ""
filedest = ""

def text_to_pdf(text, output_filename):
    pdf = canvas.Canvas(output_filename, pagesize=letter)

    pdf.setFont("Helvetica", 12)
    width, height = letter
    y_position = height - 40
    lines = text.splitlines()

    for line in lines:
        if y_position < 40:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y_position = height - 40
        pdf.drawString(40, y_position, line)
        y_position -= 14

    pdf.save()
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
def transcribe_text(doc_type):
    global filepath
    print("This is the filepath: " + filepath)
    audio_path = filepath
    transcribed_text = transcribe_audio(audio_path)
    file = open(filedest + "/transcription.txt", "w")
    file.write(transcribed_text)

def transcribe_pdf():
    global filepath
    print("This is the filepath: " + filepath)
    audio_path = filepath
    transcribed_text = transcribe_audio(audio_path)
    text_to_pdf(transcribed_text, filedest + "/transcription_output.pdf")


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
transcribetext_button = ttk.Button(mainframe, text="Transcribe to Text", command=transcribe_text).grid(column=1, row=4, sticky=N)
transcribepdf_button = ttk.Button(mainframe, text="Transcribe to PDF", command=transcribe_pdf).grid(column=2, row=4, sticky=N)
window.mainloop()