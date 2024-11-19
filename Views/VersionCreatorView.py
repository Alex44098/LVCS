import tkinter as tk
from Views.DesignElements.ScrolledText import ScrolledText


class VersionCreatorView(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.geometry("406x198+573+262")
        self.minsize(120, 1)
        self.maxsize(1540, 845)
        self.resizable(1,  1)
        self.title("Создание версии")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.025, rely=0.051, height=21, width=74)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Имя версии:''')

        self.name_entry = tk.Entry(self)
        self.name_entry.place(relx=0.222, rely=0.051, height=20, relwidth=0.749)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(highlightbackground="#d9d9d9")
        self.name_entry.configure(highlightcolor="#000000")
        self.name_entry.configure(insertbackground="#000000")
        self.name_entry.configure(selectbackground="#d9d9d9")
        self.name_entry.configure(selectforeground="black")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.025, rely=0.202, height=21, width=64)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Описание:''')

        self.desc_text = ScrolledText(self)
        self.desc_text.place(relx=0.222, rely=0.202, relheight=0.475, relwidth=0.749)

        self.desc_text.configure(background="white")
        self.desc_text.configure(font="TkTextFont")
        self.desc_text.configure(foreground="black")
        self.desc_text.configure(highlightbackground="#d9d9d9")
        self.desc_text.configure(highlightcolor="#000000")
        self.desc_text.configure(insertbackground="#000000")
        self.desc_text.configure(selectbackground="#d9d9d9")
        self.desc_text.configure(selectforeground="black")
        self.desc_text.configure(wrap="word")

        self.create_button = tk.Button(self)
        self.create_button.place(relx=0.271, rely=0.758, height=36, width=187)
        self.create_button.configure(activebackground="#d9d9d9")
        self.create_button.configure(activeforeground="black")
        self.create_button.configure(background="#d9d9d9")
        self.create_button.configure(disabledforeground="#a3a3a3")
        self.create_button.configure(foreground="#000000")
        self.create_button.configure(highlightbackground="#d9d9d9")
        self.create_button.configure(highlightcolor="#000000")
        self.create_button.configure(text='''Создать''')

    # Get window elements
    def get_fields(self):
        fields = {
            "name_text": self.name_entry,
            "desc_text": self.desc_text
        }
        return fields
