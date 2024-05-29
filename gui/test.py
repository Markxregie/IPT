import tkinter

window = tkinter.Tk()
window.title("Radio button")

def radioclicked():
    intvalue = vargender.get()
    if intvalue == 1:
        selected = "You Are Male"
    elif intvalue == 2:
        selected = "Your Are Female"
        label1.config(text= selected)


window = tkinter.Tk()
vargender = tkinter.IntVar()

tkinter.Label(window, text = "Gender", justify = tkinter.LEFT, padx = 20).pack()

tkinter.Radiobutton(window, text = "Male", padx = 20, variable = vargender, value = 1).pack(anchor = tkinter.W)
tkinter.Radiobutton(window, text = "Female", padx = 20, variable = vargender, value = 1).pack(anchor = tkinter.W)

button1 = tkinter.Button(window, text = "OK", command = radioclicked).pack()

label1 = tkinter.Label(window, text = "")
label1.pack()



window.mainloop()