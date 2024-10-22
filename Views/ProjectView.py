import tkinter as tk
from Views.DesignElements import ScrolledFileTree
import os


class ProjectView(tk.Toplevel):
    def __init__(self, parent, path):
        tk.Toplevel.__init__(self, parent)
        self.title("Проект")
        self.geometry("1000x600+100+50")
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        self.abspath = os.path.abspath(path)

        self.nodes = {}
        self.tree = ScrolledFileTree.ScrolledTreeView(self)
        self.tree.place(relx=0.014, rely=0.022, relheight=0.7, relwidth=0.4)
        self.tree.heading("#0", text=self.abspath, anchor=tk.W)

        self.tree.bind("<<TreeviewOpen>>", self.open_node)
        self.populate_node("", self.abspath)

    def populate_node(self, parent, abspath):
        for entry in os.listdir(abspath):
            entry_path = os.path.join(abspath, entry)
            node = self.tree.insert(parent, tk.END, text=entry, open=False)
            if os.path.isdir(entry_path):
                self.nodes[node] = entry_path
                self.tree.insert(node, tk.END)

    def open_node(self, event):
        item = self.tree.focus()
        path = self.nodes.pop(item, False)
        if path:
            children = self.tree.get_children(item)
            self.tree.delete(children)
            self.populate_node(item, path)
