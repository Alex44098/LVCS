from Views.DesignElements import AutoScroll
import tkinter as tk


class ScrolledText(AutoScroll.AutoScroll, tk.Text):
    # A standard Tkinter Text widget with scrollbars that will
    # automatically show/hide as needed.
    @AutoScroll.create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.AutoScroll.__init__(self, master)