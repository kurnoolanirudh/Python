import tkinter as tk

# tk._test() # to get a test ui
#

root = tk.Tk()

# root.mainloop()  # will give a blank window

# to set the title of the UI
root.title("LEARN")

# to put a label on top a button
lbl = tk.Label(root, text="Press Here : ")
lbl.grid()  # this geometry manager will add the label to the window

# to put a button
btn = tk.Button(root, text="Button")
btn.grid()  # this geometry manager will add the button to the window

# to put the label beside a button
lbl1 = tk.Label(root, text="Press Here : ")
lbl1.grid(row=2, column=0)

btn1 = tk.Button(root, text="Button1")
btn1.grid(row=2, column=1)


# to execute some function when the button is clicked
def btn_on_click():
    print("testing")


def change_label_on_click():
    _ = lbl2.config(text="Button3 Clicked")


lbl2 = tk.Label(root, text="Press Here : ")
lbl2.grid(row=3, column=0)

btn2 = tk.Button(root, text="Button2", command=btn_on_click)
btn2.grid(row=3, column=1)

btn3 = tk.Button(root, text="Button3", command=change_label_on_click)
btn3.grid(row=3, column=3)

# to see all available attributes on labels
print(lbl2.config().keys())

# frame is a container for other widgets
frame = tk.Frame(root)
frame.grid(row=4, column=0)

entry = tk.Entry(frame)  # to put this entry in the frame
entry.grid(
    row=0, column=0
)  # this geometry is applied with repsect to the frame i.e. inside the frame

entry_btn = tk.Button(frame, text="Add")
entry_btn.grid(row=0, column=3)

entry_text_list = tk.Listbox(frame)
entry_text_list.grid(row=1, column=0)

root.mainloop()
