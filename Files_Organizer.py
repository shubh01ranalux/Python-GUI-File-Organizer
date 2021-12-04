from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os
from pathlib import Path

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "Presentations" :[".ppt", "pptx"],  
    "Word Documents": [".docx", ".doc"],
    "Excel Sheets": [".xls", ".xlsx"],
    "Other Documents": [".oxps", ".epub", ".pages", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd" ],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Texts": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "Python": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "Shell": [".sh"] 
}
 
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
 

root = Tk()
root.geometry('300x100')
root.title('Files Organizer')
root['bg']='#5d8a82'
f = ("Comic Sans", 14)

def dirsel():
    global folder_path
    currdir = os.getcwd()
    folder_path = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    Label(root, text=f'Selected Directory: {folder_path}').grid(row = 2, column=0)
    
def organize():
    global folder_path
    no_of_files=len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
    seldir = os.scandir(folder_path)
    i=0
    while i<no_of_files:
        for entry in seldir:
            if entry.is_dir():
                continue
            file_path = Path(entry)
            file_format = file_path.suffix.lower()
            if file_format in FILE_FORMATS:
                directory_path = os.path.join(folder_path,(FILE_FORMATS[file_format]))
                directory_path = Path(directory_path)
                if os.path.isdir(directory_path)== False:
                    os.mkdir(directory_path)
                    filename=os.path.basename(file_path)
                    new_file_path=os.path.join(directory_path,filename)
                    os.rename(file_path, new_file_path)
                else:
                    filename=os.path.basename(file_path)
                    new_file_path=os.path.join(directory_path,filename)
                    os.rename(file_path, new_file_path)
        i+=1


Button(root, text ="Choose Directory", font=f, command = dirsel).grid(row = 1, column=0)
Button(root, text ="Organize", font=f, command = organize).grid(row = 3, column=0)

root.mainloop()
