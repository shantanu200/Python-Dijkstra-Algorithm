from matplotlib.pyplot import text
from main import binarySearch,dijkstara,getCityList
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
starttext = ""
endtext = ""
def mainPage():
    root.geometry("800x500")
    root.title("Path Finder")
    root.config(background="white")
    root.resizable(0,0)

    header = Label(root,text="PATH FINDER",fg="white",bg="black",width=48,font=("Code New Roman",20,"bold"))
    header.place(x=0,y=2)
    
    startLabel = Label(root,text="Enter Starting Destination:",font=("Code New Roman",14,"bold"),fg="black",bg="white")
    startLabel.place(x=250,y=70)  
    start = Entry(root,textvariable=starttext,font=("Code New Roman",12),width=30)
    start.place(x=250,y=100)

    endLabel = Label(root,text="Enter Ending Destination:",font=("Code New Roman",14,"bold"),fg="black",bg="white")
    endLabel.place(x=250,y=130)  
    end = Entry(root,textvariable=starttext,font=("Code New Roman",12),width=30)
    end.place(x=250,y=160)

    def getData():
        e_start = start.get()
        e_end = end.get()

        e_start = e_start.lower()
        e_end = e_end.lower()

        start_index = binarySearch(0,4,e_start)
        end_index = binarySearch(0,4,e_end)
        label1 = ""
        label2 = ""
         
        
        if(e_start == "" or e_end == ""):
            mb.showerror("Empty","Please Fill all the fields")
        elif(start_index == -1 or end_index==-1):
            mb.showerror("Not Found","No such city found in list")
        else:
            ans = dijkstara(start_index,end_index)
            label1 = str(ans[0])
            label2 = str(ans[1])

            

        ans1 = Label(root,font=("Code New Roman",14,"bold"),fg="black",bg="white")
        ans1.config(text=label1)
        ans1.place(x=250,y=300)
    
        ans2 = Label(root,font=("Code New Roman",14,"bold"),fg="black",bg="white")
        ans2.config(text=label2)
        ans2.place(x=250,y=350)    

            
            
            
            
        
        
    searchButton = Button(root,text="SEARCH",font=("Code New Roman",15,"bold"),fg="white",bg="green",width=15,command=getData)
    searchButton.place(x=300,y=200)

    root.mainloop()
