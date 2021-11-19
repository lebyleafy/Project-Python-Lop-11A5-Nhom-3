import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib
import pyttsx3
window = tk.Tk()

window.title("PDF File Converter (text only)")


def converttodoc():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    pathlib.Path('context.doc').write_text(page_content)
    showinfo("Done", "Successfully Converted")

def converttotext():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    pathlib.Path('context.txt').write_text(page_content)
    showinfo("Done", "Successfully Converted")

def converttotts():
    file = askopenfile(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = open(file.name, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    no_of_pages = read_pdf.getNumPages()
    page = read_pdf.getPage(0)
    page_content = page.extractText()
    speak = pyttsx3.init()
    speak.say(page_content)
    speak.runAndWait()


label = tk.Label(window, text="Convert to DOC: ")
label.grid(row=0, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=35, command=converttodoc)
button.grid(row=0, column=1, padx=5, pady=5)



label = tk.Label(window, text="Convert to TXT: ")
label.grid(row=1, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=35, command=converttotext)
button.grid(row=1, column=1, padx=5, pady=5)



label = tk.Label(window, text="Read the PDF file: ")
label.grid(row=2, column=0, padx=5, pady=5)

button = ttk.Button(window, text="Select", width=35, command=converttotts)
button.grid(row=2, column=1, padx=5, pady=5)

label = tk.Label(window, text="Developed by Nguyễn Duy An")
label.grid(row=3, column=0, padx=5, pady=5)
label.config(font=("Courier", 7))


window.mainloop()