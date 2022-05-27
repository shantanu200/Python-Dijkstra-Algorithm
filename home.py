from logging import root
from tkinter import *
from turtle import window_height
from PIL import Image,ImageTk

app = Tk()

def appGui():
    app.geometry("800x500")
    app.title("Path Finder")
    app.resizable(0,0)
    app.config(background="white")

    img = PhotoImage(file="E:\\SEMESTER 04\\AdityaGUI\\bg.png")
    image_label = Label(app,image=img,bg="white")
    image_label.pack(pady=(20,0))

    header = Label(app,text="PATH FINDER",width=48,bg="black",fg="white",font=("Code New Roman",20,"bold"))
    header.place(x=0,y=2)

    startButton = Button(app,text="START",font=("Code New Roman",14,"bold"),bg="green",width=15)
    startButton.place(x=100,y=200)
    app.mainloop()

appGui()

