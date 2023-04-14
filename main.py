import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

FILEOPENOPTIONS = dict(defaultextension=".pdf", filetypes=[('pdf file', '*.pdf')])
# file_path = filedialog.askopenfilename(FILEOPENOPTIONS)
path = filedialog.askopenfilename(**FILEOPENOPTIONS)
# path of the PDF file
# path = open('file.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
# from_page = pdfReader.pages[]

# Instead will make it read out the full pdf. in the future can make it so user can select what page to what page
# # print(pdfReader.numPages)       #deprecated
# print(len(pdfReader.pages))
text = ""
for i in range(len(pdfReader.pages)):
    from_page = pdfReader.pages[i]
    text += from_page.extract_text()
    print(text)

# extracting the text from the PDF
# text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()