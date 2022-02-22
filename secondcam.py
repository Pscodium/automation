import tkinter as tk
from tkinter import *
import socket
import threading
from vidstream import *


local_ip = socket.gethostbyname(socket.gethostname())
print(local_ip)

server = StreamingServer(local_ip, 7777)
receiver = AudioReceiver(local_ip, 6666)


def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)

    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text.get(1.0, 'end-1c'), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start() ###feito

def start_screen_sharing():
    screen_sharing_client = ScreenShareClient(text.get(1.0, 'end-1c'), 9999)
    t4 = threading.Thread(target=screen_sharing_client.start_stream)
    t4.start() ###feito

def start_audio_stream():
    audio_sender = AudioSender(text.get(1.0, 'end-1c'), 8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start() ###feito

        
window = tk.Tk()
window.title('WebRTC Player')
window.geometry('300x300')
window.configure(bg='white')

label = Label(window, text='Endereço de ip')
label.pack()

text = Text(window, height=1)
text.pack()

listen = Button(window, text='Comece à ouvir', command=start_listening)
listen.pack(anchor=CENTER, expand=True)

camera = Button(window, text='Câmera ao vivo', command=start_camera_stream)
camera.pack(anchor=CENTER, expand=True)

share = Button(window, text='Compartilhe sua Câmera', command=start_screen_sharing)
share.pack(anchor=CENTER, expand=True)

audio = Button(window, text='Compartilhe seu áudio', command=start_audio_stream)
audio.pack(anchor=CENTER, expand=True)            

        
window.mainloop()




