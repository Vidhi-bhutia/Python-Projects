import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    filename = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Saved", "File saved successfully!")

root = tk.Tk()
root.title("My Text Editor")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 14),fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()