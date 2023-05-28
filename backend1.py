import tkinter as tk
import requests
import json
from tkinter import *
from tkinter import messagebox

API_URL = "<API_URL>"
API_KEY = "<API_KEY>"


def summarize():
    def summarize():
        video_url = entry1.get()
        text_url = entry2.get()
        sound_url = entry3.get()

        if video_url:
            prompt = f"Summarize video: {video_url}. Please summarize this link."
            response = chatgpt_api_request(prompt)
            # Process the response and display the result in the text box

        if text_url:
            prompt = f"Summarize text: {text_url}. Please summarize this link."
            response = chatgpt_api_request(prompt)
            # Process the response and display the result in the text box

        if sound_url:
            prompt = f"Summarize audio: {sound_url}. Please summarize this link."
            response = chatgpt_api_request(prompt)
            # Process the response and display the result in the text box

    def chatgpt_api_request(prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        data = {
            "inputs": {
                "prompt": prompt
            }
        }
        response = requests.post(API_URL, headers=headers, json=data)
        response_data = json.loads(response.content)
        return response_data["result"]


def chatgpt_api_request(task, url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "inputs": {
            "task": task,
            "url": url
        }
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = json.loads(response.content)
    return response_data["result"]


root = Tk()
root.geometry("640x480")
root.wm_title("Multimedia to Text Program V.0.01")
logo = tk.PhotoImage(file="logo.png")
tk.Label(root, image=logo).pack(side="right")

l1 = tk.Label(root, text='Video URL\n', font="Helvetica 16 bold")
l1.pack()

canvas1 = tk.Canvas(root, width=100, height=10)
canvas1.pack()

entry1 = tk.Entry(root, width=50)
canvas1.create_window(50, 0, window=entry1)

l2 = tk.Label(root, text='Text URL\n', font="Helvetica 16 bold")
l2.pack()

canvas2 = tk.Canvas(root, width=100, height=10)
canvas2.pack()

entry2 = tk.Entry(root, width=50)
canvas2.create_window(50, 0, window=entry2)

l3 = tk.Label(root, text='Audio URL\n', font="Helvetica 16 bold")
l3.pack()

canvas3 = tk.Canvas(root, width=100, height=30)
canvas3.pack()

entry3 = tk.Entry(root, width=50)
canvas3.create_window(50, 0, window=entry3)

btn = Button(root, text='Summarize!', command=summarize)
btn.place(x=145, y=200)

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)
textBox = Text(width=40, height=15, x=150, y=210, yscrollcommand=scroll_bar.set)
textBox.pack(side=BOTTOM)

root.mainloop()
