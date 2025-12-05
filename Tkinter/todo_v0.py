import tkinter as tk

root = tk.Tk()


def add_to_list():
    text = entry.get()
    if text:
        entry_text_list.insert(tk.END, text)
        # clear out the text entry are after successfully adding the entry to the list
        entry.delete(0, tk.END)


def add_to_list_enter_key(event=None):
    text = entry.get()
    if text:
        entry_text_list.insert(tk.END, text)
        # clear out the text entry are after successfully adding the entry to the list
        entry.delete(0, tk.END)


# to expand the elements with respect to the window size
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
# frame.grid(row=0, column=0)
# sticky argument tells in which directions the element should expand (nsew = north south east west)
# padx and pady give padding to the UI elements
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = tk.Entry(frame)  # to put this entry in the frame
# this geometry is applied with repsect to the frame i.e. inside the frame
entry.grid(row=0, column=0, sticky="ew")

# to add to the list after user types the todo and presses enter
_ = entry.bind("<Return>", add_to_list_enter_key)


entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=2)

entry_text_list = tk.Listbox(frame)
# entry_text_list.grid(row=1, column=0)
entry_text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")


root.mainloop()
