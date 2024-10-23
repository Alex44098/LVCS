from Views.DesignElements import AutoScroll
from tkinter import ttk


class ScrolledTreeView(AutoScroll.AutoScroll, ttk.Treeview):
    # A standard ttk Treeview widget with scrollbars that will
    # automatically show/hide as needed.
    @AutoScroll.create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.AutoScroll.__init__(self, master)


