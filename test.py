from tkinter import *

root = Tk()

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.place()
        self.spicok = ''
        self.erase = []
        self.create_widgets()

    def create_widgets(self):
        Label(self,text = 'Вставь значения в поле ниже.',font=("Helvetica", 20) ).place(x=0,y=0)
        self.values = Text(self,width=25,height = 20, font=("Helvetica", 20), highlightbackground = 'black')
        self.values.place()

        self.exit = Text(self,width=25,height = 20,font=("Helvetica", 20), highlightbackground = 'black')
        self.exit.place()


        self.bttn = Button(self, text = 'Преобразовать и\n скопировать',font=("Helvetica", 20), wraplength = 160)
        self.bttn.place()

        self.bttn2 =Button(self,text = 'Очистить',font=("Helvetica", 20))
        self.bttn2.place()






root.geometry('600x800')
app = Application(root)
root.mainloop()