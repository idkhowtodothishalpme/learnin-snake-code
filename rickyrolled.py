import webbrowser
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Congratulations!", "You have been selected as today's lucky winner!\n\nClick OK to claim your prize!")

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

messagebox.showinfo("Enjoy!", "Never gonna give you up ;)")