from tkinter import *

root = Tk()

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.spicok = ''
        self.erase = []
        self.create_widgets()

    def create_widgets(self):

        Label(self.frame,text = 'Вставь значения в поле ниже.',font=("Helvetica", 20) ).grid(row = 0, column = 0, sticky = W)
        self.values = Text(self.frame,width=25,height = 22, font=("Helvetica", 20), highlightbackground = 'black')
        self.values.grid(row = 1 ,column = 0)
        self.bttn = Button(self.frame, text = 'Преобразовать и\n скопировать', command = self.change_and_copy,font=("Helvetica", 20), wraplength = 160)
        self.bttn.grid(row = 2,column = 0)

        self.bttn2 =Button(self.frame,text = 'Очистить', command = self.delete,font=("Helvetica", 20))
        self.bttn2.grid(row = 3,column = 0)

        self.exit = Text(self.frame,width=25,height = 22,font=("Helvetica", 20), highlightbackground = 'black')
        self.exit.grid(row = 1, column = 1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def change_and_copy(self):
        values = self.values.get(0.0,END)
        values = values.split()
        self.exit.delete(0.0,END)
        self.spicok = ''
        for i in values:
            value = "'" + i +"',\n"
            self.spicok +=value

        if len(self.spicok.split()) <=1000:
            self.exit.insert(0.0,self.spicok[:-2])
            self.clipboard_clear()
            self.clipboard_append(self.spicok[:-2])

        elif len(self.spicok.split()) >1000:
            self.exit.insert(0.0,self.spicok[:-2])
            self.clipboard_clear()
            split = self.spicok.split()
            split1000 = split[:1000]
            split1000 = "\n".join(split1000)
            self.clipboard_append(split1000[:-1])
            for i in range(int(len(split)/1000)):
                strer = str(i + 1)
                text = "Скопировать следующую тысячу " + strer
                self.i = Button(self.frame, text = text, command = lambda i=i: self.copies(i))
                self.i.grid(row = 4 +i, column = 0)
                self.erase.append(self.i)

    def copies(self,i):
        split = self.spicok.split()
        split = split[(i+1)*1000:(i+2)*1000]
        split = "\n".join(split)
        self.clipboard_clear()
        self.clipboard_append(split[:-1])



    def delete(self):
        self.exit.delete(0.0,END)
        self.values.delete(0.0,END)
        self.spicok =''
        for i in self.erase:
            i.destroy()

root.geometry('600x800')
app = Application(root)
root.mainloop()


