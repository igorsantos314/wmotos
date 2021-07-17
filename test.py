from tkinter import * # Tkinter -> tkinter in Python 3

root = Tk()

#############################################################
selected = None  # This is the variable mentioned in step 1

def print_label():
    print (selected["text"] ) # This is step 3

def popup(event):
    global selected  # Tell Python that selected is global

    menu.post(event.x_root, event.y_root)

    selected = event.widget  # This is step 2
#############################################################

# create a popup menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Display the label", command=print_label)

# create the 3 labels
label1_text=StringVar()
label2_text=StringVar()
label3_text=StringVar()

label1_text.set("my label 1")
label2_text.set("my label 2")
label3_text.set("my label 3")

label1=Label(root, textvariable=label1_text)
label2=Label(root, textvariable=label2_text)
label3=Label(root, textvariable=label3_text)

label1.pack()
label2.pack()
label3.pack()

# attach popup to frame
label1.bind("<Button-3>", popup)
label2.bind("<Button-3>", popup)
label3.bind("<Button-3>", popup)

root.mainloop()