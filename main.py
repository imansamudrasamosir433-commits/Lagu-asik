import tkinter as tk
import time
import threading
from pygame import mixer # Library untuk putar musik

# Lirik dan detiknya (sesuaikan dengan lagu)
lyrics = [
    (10, "Kan ku terabas api neraka"),
    (13, "Untuk bisa menatap matamu hari ini"),
    (16, "Badai petir di atas kepala"),
    # Tambahkan lirik lainnya di sini...
]

def typewriter_effect(text, label):
    label.config(text="")
    for char in text:
        label.config(text=label.cget("text") + char)
        time.sleep(0.08) # Kecepatan ketik

def play_lyrics(label):
    mixer.init()
    mixer.music.load("perseverance.mp3") 
    mixer.music.play()
    
    start_time = time.time()
    for timestamp, text in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.1)
        typewriter_effect(text, label)

# GUI Setup
root = tk.Tk()
root.title("Perseverance - Hindia")
root.geometry("500x300")
root.configure(bg="black")

label = tk.Label(root, text="", fg="white", bg="black", font=("Times New Roman", 18, "bold"))
label.pack(expand=True)

# Menjalankan fungsi lirik di thread berbeda
threading.Thread(target=play_lyrics, args=(label,)).start()

root.mainloop()
