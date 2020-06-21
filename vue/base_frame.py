from tkinter import Frame, Label, Entry, DISABLED
from functools import partial
from tkinter import ttk


class BaseFrame(Frame):
    def __init__(self, root_frame):
        super().__init__(root_frame.master)
        self._root_frame = root_frame

    def show(self):
        self.pack(padx=10, pady=10)

    def hide(self):
        self.pack_forget()

    def quit(self):
        self._root_frame.quit()

    def back(self):
        self._root_frame.back()

    def create_entry(self, label, row=0, width=50, validate_callback=None, text=None,
                     disabled=False, columnspan=3, **options):
        Label(self, text=label).grid(row=row, sticky="w")
        entry = Entry(self, width=width, fg='black', **options)
        if text:
            entry.insert(0, text)
        if disabled:
            entry.config(state=DISABLED)
        if validate_callback:
            entry.bind('<KeyRelease>', partial(validate_callback, entry=entry))
        entry.grid(row=row, column=1, columnspan=columnspan)
        return entry

    def create_comboBox(self, label, row, current,
                        disabled=False, **options):
        Label(self, text=label).grid(row=row, sticky="w")
        comboBox = ttk.Combobox(self,
                                values=[
                                    "",
                                    "Foot",
                                    "Curling",
                                    "Caps",
                                    "BottleFlip", ],
                                state="readonly")
        # print(dict(comboExample))
        comboBox.grid(column=1, row=row)
        comboBox.current(current)
        if disabled:
            comboBox.config(state=DISABLED)
        return comboBox

    def show_menu(self):
        self._root_frame.show_menu()
