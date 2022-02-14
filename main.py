from tkinter import *

class myProject:
    def __init__(self):
        self.window = Tk()
        self.window.title("Application")
        self.window.geometry("1024x768")   
        frame = Frame(self.window)
        frame.pack(side="top", expand=True, fill="both")

        self.Buttons()
        self.window.mainloop()
    
    def Buttons(self):
        self.clearall()
        b2= Button(self.window,text="Train", bg='light yellow', width=20,command=self.train).place(x=475,y=350)
        b1= Button(self.window,text="Predict", bg='light yellow', width=20,command=self.predict).place(x=300,y=350)

    def clearall(self):
        for widgets in self.window.winfo_children():
            widgets.destroy() 
        return
    
    def train(self):
        self.clearall()
        easy=Button(self.window,text="Easy ", bg='light yellow', width=20,command=self.f1).place(x=430,y=250)
        medium=Button(self.window,text="Medium ", bg='light yellow', width=20,command=self.f1).place(x=430,y=300)
        hard=Button(self.window,text="Hard ", bg='light yellow', width=20,command=self.f1).place(x=430,y=350)
        back=Button(self.window,text="Back ", bg='light yellow', width=20,command=self.Buttons).place(x=430,y=400)
        return
    def predict(self):
        self.clearall()
        scan=Button(self.window,text="Scan ", bg='light yellow', width=20,command=self.f1).place(x=430,y=250)
        upload=Button(self.window,text="Upload ", bg='light yellow', width=20,command=self.f1).place(x=430,y=300)
        next=Button(self.window,text="next ", bg='light yellow', width=20,command=self.next).place(x=430,y=350)
        back=Button(self.window,text="Back ", bg='light yellow', width=20,command=self.Buttons).place(x=430,y=400)

    def next(self):
        self.clearall()
        c = Canvas(self.window,bg = "white",height = 400,width=400).place(x=300,y=150)  
        blackOnWhite=Button(self.window,text="Black On White ", bg='light yellow', width=20,command=self.blackOnWhite).place(x=300,y=560)
        whiteOnblack=Button(self.window,text="White On Black ", bg='light yellow', width=20,command=self.whiteOnBlack).place(x=550,y=560)

    def blackOnWhite(self):
        self.clearall()
        T = Text(self.window, height = 5, width = 52).place(x=300,y=150)
        copy=Button(self.window,text="Copy", bg='light yellow', width=20,command=self.f1).place(x=400,y=530)
        exit=Button(self.window,text="Exit", bg='light yellow', width=20,command=self.window.destroy).place(x=400,y=560)

    def whiteOnBlack(self):
        self.clearall()
        T = Text(self.window, height = 5, width = 52).place(x=300,y=150)
        copy=Button(self.window,text="Copy", bg='light yellow', width=20,command=self.f1).place(x=400,y=530)
        exit=Button(self.window,text="Exit", bg='light yellow', width=20,command=self.window.destroy).place(x=400,y=560)

    def f1(self):
        return

obj=myProject()