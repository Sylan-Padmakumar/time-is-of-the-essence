from tkinter import *
from tkinter import ttk
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
import time
import os

#functions

class button():
    def select():
        my_notebook.select(0)

    def select2():
        my_notebook.select(1)
        
    def select3():
        my_notebook.select(2)
        
    def stop_sound():
        if stopper:
            PlaySound(None, SND_FILENAME|SND_LOOP|SND_ASYNC)
            button_snooze.destroy()         
    
class clock(button):
    def Time():
        a = time.localtime()
        h = a[3]
        m = a[4]
        s = a[5]
        global b
        b = h,":",m,":",s
        TimeLabel['text'] = b
        root.after(1000,clock.Time)
    
    def __init__() :
        global stopper
        global button_snooze
        user_alarm_time = [alarm_hour.get(),alarm_min.get(),0]
        stopper = root.after(1,clock.__init__)
        if user_alarm_time[0] == str(b[0]) and user_alarm_time[1] == str(b[2]) :
            PlaySound('alarm.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
            button_snooze = Button(my_frame2, text = "snooze", command = button.stop_sound ,pady = 50)
            button_snooze.grid() 
            root.after_cancel(stopper)


#PROGRAM BODY


#GUI


root = Tk()
root.geometry("310x300")

#FRAMES
my_notebook = ttk.Notebook(root)
my_notebook.pack()

ttk.Style().layout('TNotebook.Tab', [])

my_frame1 = Frame(my_notebook, width = 310, height = 300)
my_frame2 = Frame(my_notebook, width = 310, height = 300)
my_frame3 = Frame(my_notebook, width = 310, height = 300)

my_notebook.add(my_frame1)
my_notebook.add(my_frame2)
my_notebook.add(my_frame3)

my_frame2.grid_propagate(False)

my_button = Button(my_frame2, text = "home", command = button.select,pady = 15).grid()
my_button = Button(my_frame3, text = "home", command = button.select,pady = 15).grid()
my_button_to_alarm = Button(my_frame1, text = "alarm", command = button.select2,pady = 15).grid()
my_button3_to_timer = Button(my_frame1, text = "timer", command = button.select3,pady = 15).grid()



#CLOCK GUI
textlabel = Label(my_frame2, text= "set alarm: ", font=('Helvetica', 14))
textlabel.place(relx=0.34, rely=0.1, anchor=E)

alarm_hour = Entry(my_frame2, width = 15,borderwidth = 5,) 
alarm_hour.place(relx=0.3, rely=0.3, anchor=CENTER)

alarm_min = Entry(my_frame2, width = 15,borderwidth = 5,)
alarm_min.place(relx=0.7, rely=0.3, anchor=CENTER)



TimeLabel = Label(my_frame1,font=('Helvetica bold', 26))
TimeLabel.place(relx=0.5, rely=0.7, anchor=CENTER)

button_enter = Button(my_frame2, text = "enter", padx = 8, pady = 4,command = clock.__init__)
button_enter.place(relx=0.8, rely=0.4, anchor=CENTER)


#END

clock.Time()

root.mainloop()

#fin

