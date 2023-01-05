from tkinter import *
import time
#import os

# def update():
#    lab['text'] = randint(0,1000)
#    root.after(1000,update) 

root = Tk()

TimeLabel = Label(root)

TimeLabel.pack()


def update():
   TimeLabel['text'] = b
   root.after(1000,update)

a = time.localtime()
h = a[3]
m = a[4]
s = a[5]
b = h,":",m,":",s

update()

root.mainloop()

# while True:
#     a = time.localtime()
#     h = a[3]
#     m = a[4]
#     s = a[5]
#     b = h,":",m,":",s
#     update()
#     #time.sleep(1)
#     #os.system('cls')