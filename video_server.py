#Audio, video and Screen sharing and necessary libraries
from vidstream import *
import tkinter as tk
import socket
import  threading
import requests

local_ip = socket.gethostbyname(socket.gethostname())
print(local_ip)

#GUI
window = tk.Tk()
window.title("Video Chat Room with mining crypto")
window.geometry('300x200')

label_target_ip = tk.Label(window, text = "Target IP:  ")
label_target_ip.pack()

text_target_ip = tk.Text(window, height = 1)
text_target_ip.pack()

btn_listen = tk.Button(window, text = "start listening", width=50)
btn_listen.pack(anchor=tk.CENTER, expand=True) 

btn_camera = tk.Button(window, text = "start Camera Stream", width=50)
btn_camera.pack(anchor=tk.CENTER, expand=True) 

btn_stream = tk.Button(window, text = "start Screen Sharing", width=50)
btn_stream.pack(anchor=tk.CENTER, expand=True) 

btn_audio = tk.Button(window, text = "start Audio Stream", width=50)
btn_audio.pack(anchor=tk.CENTER, expand=True) 

window.mainloop()






