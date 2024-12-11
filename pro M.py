import tkinter as tk
from gtts import gTTS

import playsound
import os


def text_to_speech():
    text = entry.get()
    if text.strip():  
        tts = gTTS(text=text, lang='en')
        audio_file = "speech.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)


def clear_text():
    entry.delete(0, tk.END)


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Text to Speech")
root.geometry("500x500")  

label = tk.Label(root, text="Text to speech", font=("Arial", 14))
label.pack(pady=20)


entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=30)


play_button = tk.Button(button_frame, text="Play", command=text_to_speech, bg="green", fg="white", width=10, height=2)
play_button.grid(row=0, column=0, padx=20)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="red", fg="white", width=10, height=2)
exit_button.grid(row=0, column=1, padx=20)

set_button = tk.Button(button_frame, text="Set ", command=clear_text, bg="blue", fg="white", width=10, height=2)
set_button.grid(row=0, column=2, padx=20)


root.mainloop()