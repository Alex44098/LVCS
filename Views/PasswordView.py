import tkinter as tk


class PasswordView(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.geometry("303x110+637+327")
        self.minsize(120, 1)
        self.maxsize(1540, 845)
        self.resizable(1,  1)
        self.title("Пароль")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.033, rely=0.109, height=17, width=55)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Пароль:''')

        self.password_entry = tk.Entry(self)
        self.password_entry.place(relx=0.231, rely=0.109, height=20, relwidth=0.706)
        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="#000000")
        self.password_entry.configure(insertbackground="#000000")
        self.password_entry.configure(selectbackground="#d9d9d9")
        self.password_entry.configure(selectforeground="black")

        self.apply_button = tk.Button(self)
        self.apply_button.place(relx=0.132, rely=0.455, height=46, width=227)
        self.apply_button.configure(activebackground="#d9d9d9")
        self.apply_button.configure(activeforeground="black")
        self.apply_button.configure(background="#d9d9d9")
        self.apply_button.configure(disabledforeground="#a3a3a3")
        self.apply_button.configure(foreground="#000000")
        self.apply_button.configure(highlightbackground="#d9d9d9")
        self.apply_button.configure(highlightcolor="#000000")
        self.apply_button.configure(text='''Открыть проект''')

    # Get window elements
    def get_fields(self):
        fields = {
            "password_text": self.password_entry
        }

        return fields
