from tkinter import *



app = Tk()
def destroyWindows():
    app.destroy()
    from gui import mainPage
    mainPage()

def appGui():
    app.geometry("800x500")
    app.title("Path Finder")
    app.resizable(0,0)
    app.config(background="white")

    img = PhotoImage(file="E:\\SEMESTER 04\\AdityaGUI\\bg.png")
    image_label = Label(app,image=img,bg="white")
    image_label.pack(pady=(100,0))

    header = Label(app,text="PATH FINDER",width=48,bg="black",fg="white",font=("Code New Roman",20,"bold"))
    header.place(x=0,y=2)

    startButton = Button(app,text="START",font=("Code New Roman",14,"bold"),bg="green",width=15,fg="white",command=destroyWindows)
    startButton.place(x=300,y=400)
    app.mainloop()

appGui()


