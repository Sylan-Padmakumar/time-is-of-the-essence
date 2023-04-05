from tkinter import *
import time

class clock():
    def Time():
        a = time.localtime()
        h = a[3]
        m = a[4]
        s = a[5]
        global b
        b = h,":",m,":",s
        TimeLabel['text'] = b
        root.after(1000,clock.Time)

root = Tk()
root.geometry("240x210")
root.title("clock")
root.configure(background= "#34495E" )

photo = PhotoImage(file = "C:/Users/psypa/Documents/python/dev python/clock app/images.png")
root.iconphoto(False, photo)

TimeLabel = Label(root,font=('Helvetica bold', 30, ),fg = "#F7F9F9",bg = "#34495E")
TimeLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

clock.Time()

root.mainloop()
