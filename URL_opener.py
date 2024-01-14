import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

root=tk.Tk()
root.title("URL Opener")
root.configure(bg='black')

def search_youtube():
    query = entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query = entry.get()
    url=f"http://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_instagram():
    username = entry.get().replace('@','')
    url=f"www.instagram.com/{username}"
    webbrowser.open(url)

def search_linkedin():
    username = entry.get().replace('@', '')
    url=f"www.linkedin.com/in/{username}"
    webbrowser.open(url)

Label(root, text="Enter Your Command: ").pack(pady=10)
entry = Entry(root, width=50)
entry.pack(padx=20, pady=10)
Button(root, text="Search YouTube", command=search_youtube).pack(pady=5)
Button(root, text="Search Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)
Button(root, text="View LinkedIn Profile", command=search_linkedin).pack(pady=5)

root.mainloop()
