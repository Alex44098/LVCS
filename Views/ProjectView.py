import tkinter as tk
from tkinter import ttk
from Views.DesignElements import ScrolledFileTree
from Views.DesignElements import ScrolledText
import os


class ProjectView(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        # Main settings
        self.title("Проект")
        self.geometry("1000x600+100+50")
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.abspath = None
        self.combobox = tk.StringVar()

        # Setting directory tree
        self.nodes = {}
        self.tree = ScrolledFileTree.ScrolledTreeView(self)
        self.tree.place(relx=0.014, rely=0.022, relheight=0.7, relwidth=0.4)
        # self.tree.heading("#0", text=self.abspath, anchor=tk.W)

        self.tree.bind("<<TreeviewOpen>>", self.open_node)
        # self.populate_node("", self.abspath)

        # Setting file viewer
        self.scrolled_text = ScrolledText.ScrolledText(self)
        self.scrolled_text.place(relx=0.43, rely=0.017, relheight=0.688, relwidth=0.563)
        self.scrolled_text.configure(background="white")
        self.scrolled_text.configure(font="TkTextFont")
        self.scrolled_text.configure(foreground="black")
        self.scrolled_text.configure(highlightbackground="#d9d9d9")
        self.scrolled_text.configure(highlightcolor="#000000")
        self.scrolled_text.configure(insertbackground="#000000")
        self.scrolled_text.configure(insertborderwidth="3")
        self.scrolled_text.configure(selectbackground="#d9d9d9")
        self.scrolled_text.configure(selectforeground="black")
        self.scrolled_text.configure(wrap="none")

        # Simple separator decoration
        self.separator = ttk.Separator(self)
        self.separator.place(relx=0.0, rely=0.733, relwidth=1.0)

        # Current version labels
        self.Label2 = tk.Label(self)
        self.Label2.place(relx=0.02, rely=0.783, height=21, width=150)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Открытая версия проекта''')

        self.cur_version_label = tk.Label(self)
        self.cur_version_label.place(relx=0.02, rely=0.85, height=40, width=150)
        self.cur_version_label.configure(activebackground="#d9d9d9")
        self.cur_version_label.configure(activeforeground="black")
        self.cur_version_label.configure(anchor='center')
        self.cur_version_label.configure(background="#d9d9d9")
        self.cur_version_label.configure(compound='center')
        self.cur_version_label.configure(disabledforeground="#a3a3a3")
        self.cur_version_label.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.cur_version_label.configure(foreground="#000000")
        self.cur_version_label.configure(highlightbackground="#d9d9d9")
        self.cur_version_label.configure(highlightcolor="#000000")
        self.cur_version_label.configure(text='''Локальная''')

        # Versions label
        self.Label1 = tk.Label(self)
        self.Label1.place(relx=0.20, rely=0.783, height=21, width=104)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Версии проекта:''')

        # Versions combobox
        self.versions_combobox = ttk.Combobox(self)
        self.versions_combobox.place(relx=0.33, rely=0.783, relheight=0.032, relwidth=0.267)
        self.versions_combobox.configure(font="-family {Segoe UI} -size 9")
        self.versions_combobox.configure(textvariable=self.combobox)

        # Select version button
        self.select_version_button = tk.Button(self)
        self.select_version_button.place(relx=0.25, rely=0.85, height=56, width=277)

        self.select_version_button.configure(activebackground="#d9d9d9")
        self.select_version_button.configure(activeforeground="black")
        self.select_version_button.configure(background="#d9d9d9")
        self.select_version_button.configure(disabledforeground="#a3a3a3")
        self.select_version_button.configure(font="-family {Segoe UI} -size 9")
        self.select_version_button.configure(foreground="#000000")
        self.select_version_button.configure(highlightbackground="#d9d9d9")
        self.select_version_button.configure(highlightcolor="#000000")
        self.select_version_button.configure(text='''Открыть выбранную версию''')

        # New version button
        self.new_version_button = tk.Button(self)
        self.new_version_button.place(relx=0.625, rely=0.80, height=80, width=150)

        self.new_version_button.configure(activebackground="#d9d9d9")
        self.new_version_button.configure(activeforeground="black")
        self.new_version_button.configure(background="#d9d9d9")
        self.new_version_button.configure(disabledforeground="#a3a3a3")
        self.new_version_button.configure(font="-family {Segoe UI} -size 9")
        self.new_version_button.configure(foreground="#000000")
        self.new_version_button.configure(highlightbackground="#d9d9d9")
        self.new_version_button.configure(highlightcolor="#000000")
        self.new_version_button.configure(text='''Новая версия''')

        # Open file button
        self.open_file_button = tk.Button(self)
        self.open_file_button.place(relx=0.80, rely=0.80, height=80, width=150)

        self.open_file_button.configure(activebackground="#d9d9d9")
        self.open_file_button.configure(activeforeground="black")
        self.open_file_button.configure(background="#d9d9d9")
        self.open_file_button.configure(disabledforeground="#a3a3a3")
        self.open_file_button.configure(font="-family {Segoe UI} -size 9")
        self.open_file_button.configure(foreground="#000000")
        self.open_file_button.configure(highlightbackground="#d9d9d9")
        self.open_file_button.configure(highlightcolor="#000000")
        self.open_file_button.configure(text='''Открыть файл''')

    def set_project_path(self, path):
        self.abspath = os.path.abspath(path)
        self.tree.heading("#0", text=self.abspath, anchor=tk.W)
        self.populate_node("", self.abspath)

    # Creating of directory tree
    def populate_node(self, parent, abspath):
        for entry in os.listdir(abspath):
            entry_path = os.path.join(abspath, entry)
            node = self.tree.insert(parent, tk.END, text=entry, open=False)
            if os.path.isdir(entry_path):
                self.nodes[node] = entry_path
                self.tree.insert(node, tk.END)

    # Opening directory in tree
    def open_node(self, event):
        item = self.tree.focus()
        path = self.nodes.pop(item, False)
        if path:
            children = self.tree.get_children(item)
            self.tree.delete(children)
            self.populate_node(item, path)

    # Get window elements
    def get_fields(self):
        fields = {
            "version_label": self.cur_version_label,
            "file_tree": self.tree,
            "text_field": self.scrolled_text,
            "versions_combobox": self.versions_combobox
        }
        return fields
