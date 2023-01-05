from tkinter import *
import time

root = Tk()

TimeLabel = Label(root)

TimeLabel.pack()


def update():
    a = time.localtime()
    h = a[3]
    m = a[4]
    s = a[5]
    b = h,":",m,":",s
    TimeLabel['text'] = b

    root.after(1000,update)


update()

root.mainloop()

