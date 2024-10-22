import tkinter as tk
from Views.DesignElements import ScrolledListBox


class ProjectManagerView(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Список проектов")
        self.geometry("1000x600+100+50")
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.Scrolledlistbox = ScrolledListBox.ScrolledListBox(self)
        self.Scrolledlistbox.place(relx=0.014, rely=0.022, relheight=0.856, relwidth=0.708)
        self.Scrolledlistbox.configure(background="white")
        self.Scrolledlistbox.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox.configure(font="TkFixedFont")
        self.Scrolledlistbox.configure(foreground="black")
        self.Scrolledlistbox.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox.configure(selectbackground="#d9d9d9")
        self.Scrolledlistbox.configure(selectforeground="black")
        # self.Scrolledlistbox.pack()

        self.Button_open = tk.Button(self)
        self.Button_open.place(relx=0.749, rely=0.022, height=66, width=167)
        self.Button_open.configure(activebackground="#d9d9d9")
        self.Button_open.configure(activeforeground="black")
        self.Button_open.configure(background="#d9d9d9")
        self.Button_open.configure(disabledforeground="#a3a3a3")
        self.Button_open.configure(foreground="#000000")
        self.Button_open.configure(highlightbackground="#d9d9d9")
        self.Button_open.configure(highlightcolor="#000000")
        self.Button_open.configure(text='''Открыть''')
        # self.Button_open.pack()

        self.Button_create = tk.Button(self)
        self.Button_create.place(relx=0.749, rely=0.2, height=76, width=167)
        self.Button_create.configure(activebackground="#d9d9d9")
        self.Button_create.configure(activeforeground="black")
        self.Button_create.configure(background="#d9d9d9")
        self.Button_create.configure(disabledforeground="#a3a3a3")
        self.Button_create.configure(foreground="#000000")
        self.Button_create.configure(highlightbackground="#d9d9d9")
        self.Button_create.configure(highlightcolor="#000000")
        self.Button_create.configure(text='''Создать''')
        # self.Button_create.pack()

    def add_item(self, item):
        self.Scrolledlistbox.insert(0, item)
