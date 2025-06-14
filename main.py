# Music Player using Tkinter and Pygame
import tkinter as tk
import fnmatch
import os
from pygame import mixer

# Initialize mixer
mixer.init()

# Create main window
canvas = tk.Tk()
canvas.title("🎵 Modern Music Player")
canvas.geometry("500x700")
canvas.configure(bg="#1e1e1e")

# Music folder setup
rootpath = "music"
pattern = "*.mp3"

# Load control button images 
try:
    prev_img = tk.PhotoImage(file="btns/prev_img.png")
    stop_img = tk.PhotoImage(file="btns/stop_img.png")
    play_img = tk.PhotoImage(file="btns/play_img.png")
    pause_img = tk.PhotoImage(file="btns/pause_img.png")
    next_img = tk.PhotoImage(file="btns/next_img.png")
except tk.TclError:
    prev_img = stop_img = play_img = pause_img = next_img = None

# Functions
def select():
    song = listBox.get(tk.ACTIVE)
    label.config(text=f"▶️ {song}")
    mixer.music.load(os.path.join(rootpath, song))
    mixer.music.play()
    pauseButton.config(text="Pause")

def stop_music():
    mixer.music.stop()
    listBox.select_clear(tk.ACTIVE)
    label.config(text="⏹️ Stopped")

def pause_music():
    if pauseButton['text'] == "Pause":
        mixer.music.pause()
        pauseButton['text'] = "Resume"
    else:
        mixer.music.unpause()
        pauseButton['text'] = "Pause"

def next_music():
    try:
        current_index = listBox.curselection()[0]
        next_index = (current_index + 1) % listBox.size()
        listBox.select_clear(0, tk.END)
        listBox.select_set(next_index)
        listBox.activate(next_index)
        select()
    except IndexError:
        label.config(text="❌ No song selected")

def prev_music():
    try:
        current_index = listBox.curselection()[0]
        prev_index = (current_index - 1) % listBox.size()
        listBox.select_clear(0, tk.END)
        listBox.select_set(prev_index)
        listBox.activate(prev_index)
        select()
    except IndexError:
        label.config(text="❌ No song selected")

# Label
label = tk.Label(canvas, text="🎧 Select a song to play", fg="#f5c518", bg="#1e1e1e", font=("Segoe UI", 14, "bold"))
label.pack(pady=20)

# Song list
listBox = tk.Listbox(canvas, bg="#2e2e2e", fg="white", font=("Segoe UI", 12), width=45, height=15, selectbackground="#f5c518", selectforeground="black")
listBox.pack(pady=20)

# Button frame
controls = tk.Frame(canvas, bg="#1e1e1e")
controls.pack(pady=20)

# Buttons
prevButton = tk.Button(controls, image=prev_img, bg="#1e1e1e", borderwidth=0, command=prev_music)
prevButton.grid(row=0, column=0, padx=10)

stopButton = tk.Button(controls, image=stop_img, bg="#1e1e1e", borderwidth=0, command=stop_music)
stopButton.grid(row=0, column=1, padx=10)

playButton = tk.Button(controls, image=play_img, bg="#1e1e1e", borderwidth=0, command=select)
playButton.grid(row=0, column=2, padx=10)

pauseButton = tk.Button(controls, image=pause_img, text="Pause", compound=tk.TOP, fg="white", font=("Segoe UI", 8), bg="#1e1e1e", borderwidth=0, command=pause_music)
pauseButton.grid(row=0, column=3, padx=10)

nextButton = tk.Button(controls, image=next_img, bg="#1e1e1e", borderwidth=0, command=next_music)
nextButton.grid(row=0, column=4, padx=10)

# Load songs
def load_music():
    if not os.path.exists(rootpath):
        label.config(text="⚠️ 'music' folder not found.")
        return
    for root, dirs, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            listBox.insert(tk.END, filename)

load_music()
canvas.mainloop()
