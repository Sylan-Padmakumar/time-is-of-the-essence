from tkinter import *
import time
import playsound

root = Tk()
root.geometry("310x300")

textlabel = Label(root, text= "set alarm: ", font=('Helvetica', 14))
textlabel.place(relx=0.34, rely=0.1, anchor=E)

e = Entry(root, width = 45,borderwidth = 5)
e.place(relx=0.5, rely=0.2, anchor=CENTER)

TimeLabel = Label(root,font=('Helvetica bold', 26))
TimeLabel.place(relx=0.5, rely=0.5, anchor=CENTER)



def button_click():
    global h
    h = e.get()
    e.delete(0,END)
    
# button_1 = Button(root, text = "enter", padx = 40, pady = 20, command =button_click())
# button_1.place(relx=0.5, rely=0.5, anchor=CENTER)

def update():
    a = time.localtime()
    h = a[3]
    m = a[4]
    s = a[5]
    global b
    b = h,":",m,":",s
    TimeLabel['text'] = b
    root.after(1000,update)

update()

# if b == h:
#     playsound('alarm.wav')

root.mainloop()
