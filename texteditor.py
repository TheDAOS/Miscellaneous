from tkinter import *
from tkinter import filedialog

root=Tk()

text=Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "W+")
    file1.write(t)
    file1.close()
    
button=Button(root, text="Save", command=saveas)
button.grid()

root.mainloop()
