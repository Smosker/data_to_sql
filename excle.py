from tkinter import *

root = Tk()


class Application(Frame):
    """
    Приложение предназначено для преобразования строк данных в формат
    подходящий для использования в конструкциях вида 'in (data)' в oracle sql
    """
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.changed_data = []
        self.buttons_to_delete = []
        self.create_widgets()

    def on_frame_configure(self, event):
        """Обеспечивает работу scrollbar"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):

        Label(self.frame, text='Помести значения в поле ниже',
              font=("Helvetica", 20)).grid(row = 0, column = 0, sticky = W)

        self.values = Text(self.frame, width=25, height=22, font=("Helvetica", 20),
                           highlightbackground = 'black')
        self.values.grid(row=1, column=0)

        self.bttn = Button(self.frame, text='Преобразовать и\n скопировать',
                           command=self.change_and_copy, font=("Helvetica", 20),
                           wraplength=160)
        self.bttn.grid(row=2, column=0)

        self.bttn2 = Button(self.frame,text='Очистить', command=self.delete, font=("Helvetica", 20))
        self.bttn2.grid(row=3, column=0)

        self.exit = Text(self.frame, width=25, height=22, font=("Helvetica", 20),
                         highlightbackground='black')
        self.exit.grid(row=1, column=1)

    def change_and_copy(self):
        """
        Основная функция для работы с введенными данными, если входные данные
        меньше или равны 1000 строк - преобразует их, добавляет в clipboard и
        выводит на экран. Если число строк более 1000 - разбивает их по 1000
        и выводит отдельные кнопки для копирования каждой 1000 строк преобразованных
        данных.
        входные данные - 123 123 123
        выходные данные - '123',\n'123',\n'123'
        """
        values = self.values.get(0.0, END).split()
        self.exit.delete(0.0, END)
        self.changed_data.clear()
        self.changed_data = ["'" + i + "',\n" for i in values]
        result = ''.join(self.changed_data)[:-2]
        self.exit.insert(0.0, result)
        self.clipboard_clear()

        if len(self.changed_data) <= 1000:
            self.clipboard_append(result)

        else:
            first_thousand = ''.join(self.changed_data[:1000])[:-2]
            self.clipboard_append(first_thousand)

            for i in range(int(len(self.changed_data)/1000)):
                text = "Скопировать следующую тысячу " + str(i + 1)
                self.button_over_thousand = Button(self.frame, text=text, command=lambda i=i: self.copy_next_thousand(i))
                self.button_over_thousand.grid(row=4 + i, column=0)
                self.buttons_to_delete.append(self.button_over_thousand)

    def copy_next_thousand(self, i):
        """
        Используется дополнительными кнопками в случае, если количество
        строк данных более 1000, при нажатии на кнопку - копирует следующую
        1000 строк в clipboard
        """
        next_thousand = ''.join(self.changed_data[(i+1)*1000:(i+2)*1000])
        self.clipboard_clear()
        self.clipboard_append(next_thousand[:-2])

    def delete(self):
        """
        Используется для приведения приложения в изначальное состояние
        удаляет все дополнительные кнопки, очищает вход/выход
        """
        self.exit.delete(0.0, END)
        self.values.delete(0.0, END)
        self.changed_data = []
        for i in self.buttons_to_delete:
            i.destroy()

if __name__ == '__main__':
    root.geometry('620x800')
    app = Application(root)
    root.mainloop()


