# tkinter classes
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do")
        _ = self.columnconfigure(0, weight=1)
        _ = self.columnconfigure(1, weight=3)
        _ = self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        frame1 = InputForm(self)
        frame1.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(self, parent: Application):
        super().__init__(parent)

        self.entry: tk.Entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        # to add to the list after user types the todo and presses enter
        _ = self.entry.bind("<Return>", self.add_to_list_enter_key)

        self.entry_btn: tk.Button = tk.Button(
            self, text="Add", command=self.add_to_list
        )
        self.entry_btn.grid(row=0, column=2)

        self.entry_btn_1: tk.Button = tk.Button(
            self, text="Clear", command=self.clear_list
        )
        self.entry_btn_1.grid(row=0, column=3)

        self.entry_text_list: tk.Listbox = tk.Listbox(self)
        self.entry_text_list.grid(row=1, column=0, columnspan=4, sticky="nsew")

        _ = self.columnconfigure(0, weight=1)
        _ = self.rowconfigure(1, weight=1)

    def add_to_list(self):
        text = self.entry.get()
        if text:
            self.entry_text_list.insert(tk.END, text)
            # clear out the text entry are after successfully adding the entry to the list
            self.entry.delete(0, tk.END)

    def add_to_list_enter_key(self, _event=None):
        text = self.entry.get()
        if text:
            self.entry_text_list.insert(tk.END, text)
            # clear out the text entry are after successfully adding the entry to the list
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.entry_text_list.delete(0, tk.END)


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
