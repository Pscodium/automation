import tkinter as tk
from tkinter import *
import socket
import threading
from vidstream import *


black = '#000000'
white = '#ffffff'
color = '#EFFBB1'
color1 = '#CBF0AA'
color2 = '#F0A9C0'
color3 = '#CD93CF'
color4 = '#D6F72D'


local_ip = socket.gethostbyname(socket.gethostname())
print(local_ip)

server = StreamingServer(local_ip, 9999)
receiver = AudioReceiver(local_ip, 8888)

class App:
    def __init__(self):
        
        def start_listening(self):
            self.t1 = threading.Thread(target=server.start_server)
            self.t2 = threading.Thread(target=receiver.start_server)

            self.t1.start()
            self.t2.start()



        def start_camera_stream(self):
            camera_client = CameraClient(self.text.get(1.0, 'end-1c'), 7777)
            self.t3 = threading.Thread(target=camera_client.start_stream)
            self.t3.start() ###feito
            

        def start_screen_sharing(self):
            screen_sharing_client = ScreenShareClient(self.text.get(1.0, 'end-1c'), 7777)
            self.t4 = threading.Thread(target=screen_sharing_client.start_stream)
            self.t4.start() ###feito
            

        def start_audio_stream(self):
            audio_sender = AudioSender(self.text.get(1.0, 'end-1c'), 6666)
            self.t5 = threading.Thread(target=audio_sender.start_stream)
            self.t5.start() ###feito
           

        def screen(self):
       
            self.window = tk.Tk()
            self.window.title('WebRTC Player')
            self.window.geometry('300x300')
            self.window.configure(bg=color)

        def ip_adress(self):
            label = Label(self.window, bg=color, text='IP do seu amigo')
            label.place(x=10, y=10)

            self.text = Text(self.window, height=1, width=20)
            self.text.place(x=10, y=30)
        
        def buttons(self):

            listen = Button(self.window, text='Comece à ouvir', command=lambda:start_listening(self))
            listen.place(x=50, y=70)

            camera = Button(self.window, text='Câmera ao vivo', command=lambda:start_camera_stream(self))
            camera.place(x=50, y=120)

            share = Button(self.window, text='Compartilhe sua Câmera', command=lambda:start_screen_sharing(self))
            share.place(x=50, y=170)

            audio = Button(self.window, text='Compartilhe seu áudio', command=lambda:start_audio_stream(self))
            audio.place(x=50, y=220)           

            if self.window.protocol("WM_DELETE_WINDOW"):
                server.stop_server()
                receiver.stop_server()


        screen(self)
        ip_adress(self)
        buttons(self)
        
        self.window.mainloop()


app = App()

