import tkinter as tk
from Views.DesignElements import AutoScroll


class ScrolledListBox(AutoScroll.AutoScroll, tk.Listbox):
    # A standard Tkinter Listbox widget with scrollbars that will
    # automatically show/hide as needed.
    @AutoScroll.create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.AutoScroll.__init__(self, master)

    def size_(self):
        sz = tk.Listbox.size(self)
        return sz
