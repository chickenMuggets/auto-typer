#librarys
from tkinter import *
from tkinter import ttk
from ctypes import windll
import keyboard
import time
windll.shcore.SetProcessDpiAwareness(1)

screen = Tk()
#varibles
checkbutton_value = BooleanVar()
checkbutton_value.set(False)
checkbutton_value2 = BooleanVar()
checkbutton_value2.set(False)
scalevalue = IntVar()
scalevalue.set(1)

def clock():
    if checkbutton_value2.get() == True:
        amounttorepeat.place_forget()
        amounttorepeatcus.place(x=10,y=140, width=270)
    if checkbutton_value2.get() == False:
        amounttorepeat.place(x=10,y=120,width=270)
        amounttorepeatcus.place_forget()
    screen.after(1, clock) # run itself again after 1 ms

#autotyping function,

def autotyper():
    time.sleep(1)
    if checkbutton_value2.get() == True:
        for repeat in range((int(amounttorepeatcus.get()))):
            keyboard.write(inputtext.get())
            if checkbutton_value.get() == True:
                keyboard.press("ENTER")
    if checkbutton_value2.get() == False:
        print("hello")
        for repeat in range(scalevalue.get()):
            keyboard.write(inputtext.get())
            if checkbutton_value.get() == True:
                keyboard.press("ENTER")



#screen propertys
screen.title("Auto typer V5")
screen.geometry("362x550")

repeatamount = 1

#screen elements
infowrite = ttk.Label(master=screen,text="Auto typer")
labeltext = ttk.Label(master=screen,text="what do you want to be typed?")
inputtext = ttk.Entry()
amounttorepeat = ttk.LabeledScale(from_=1,to=1000,variable=scalevalue)
amounttorepeatcus = ttk.Entry()
cusamo = ttk.Checkbutton(text="custom amount", variable=checkbutton_value2)
entercheckbox = ttk.Checkbutton(text="Press enter?", variable=checkbutton_value)
startbutton = ttk.Button(text="Start", command=autotyper)

#screen element locations
infowrite.grid(row=1,column=1)
labeltext.grid(row=2,column=1)
inputtext.grid(row = 3,column = 1)
cusamo.place(x=0,y=90)
entercheckbox.place(x=0,y=200)
startbutton.place(x=0,y=250)
amounttorepeat.place(x=10,y=120,width=270)


# run first time
clock()


screen.mainloop()