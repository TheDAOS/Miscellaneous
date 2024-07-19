from tkinter import *
from tkinter import filedialog

root=Tk()

text=Text(root)
text.grid()

# Save Button
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "W+")
    file1.write(t)
    file1.close()
    
button=Button(root, text="Save", command=saveas)
button.grid()

# Font Changer
def FontHelvetica():
    global text
    text.config(font="Helvetica")
    
def FontCourier():
    global text
    text.config(font="Courier")
    
font = Menubutton(root, text="Font")
font.grid()
font.menu=Menu(font, tearoff=0)
font["menu"]=font.menu
helvetica=IntVar()
courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)

root.mainloop()
