import tkinter

import task1
from tkinter import *

root = Tk()
root.title("Task3")
root.geometry("1280x300")


label1 = Label(root, text = "Choose video resolution: ")
label1.place(x=20, y=70)

label2 = Label(root, text = "Choose video codec: ")
label2.place(x=20, y=200)

class App:
    def __init__(self):
        self.filename = ""

    def r_160x120(self):
        print("Set resolution to 160x120")
        self.filename = "bbb_160x120.mp4"

    def r_360x240(self):
        print("Set resolution to 360x240")
        self.filename = "bbb_360x240.mp4"

    def r_480p(self):
        print("Set resolution to 480p")
        self.filename = "bbb_480p.mp4"

    def r_720p(self):
        print("Set resolution to 720p")
        self.filename = "bbb_720p.mp4"

    def convert_vp8(self):
        task1.VP8(self.filename)
        print("Encoding...")

    def convert_vp9(self):
        task1.VP9(self.filename)
        print("Encoding...")

    def convert_h265(self):
        task1.h265(self.filename)
        print("Encoding...")

    def convert_av1(self):
        task1.av1(self.filename)
        print("Encoding...")


this_app = App()

#Define buttons
button1 = Button(root, text="160x120", padx = 40, pady=20, command=this_app.r_160x120, activebackground="red")
button2 = Button(root, text="360x240", padx = 40, pady=20, command=this_app.r_360x240, activebackground="red")
button3 = Button(root, text="480p", padx = 50, pady=20, command=this_app.r_480p, activebackground="red")
button4 = Button(root, text="720p", padx = 50, pady=20, command=this_app.r_720p, activebackground="red")

button5 = Button(root, text="VP8", padx = 40, pady=20, command=this_app.convert_vp8, activebackground="blue")
button6 = Button(root, text="VP9", padx = 40, pady=20, command=this_app.convert_vp9, activebackground="blue")
button7 = Button(root, text="H265", padx = 50, pady=20, command=this_app.convert_h265, activebackground="blue")
button8 = Button(root, text="AV1", padx = 50, pady=20, command=this_app.convert_av1, activebackground="blue")


#Put the buttons on the screen
button1.place(x=380, y=50)
button2.place(x=520, y=50)
button3.place(x=660, y=50)
button4.place(x=790, y=50)
button5.place(x=380, y=200)
button6.place(x=520, y=200)
button7.place(x=660, y=200)
button8.place(x=790, y=200)


root.mainloop()