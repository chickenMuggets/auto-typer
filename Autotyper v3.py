from tkinter import *
from tkinter.ttk import *
import pyautogui
import time
spammer = Tk()
useEnter = 1
pyautogui.FAILSAFE = TRUE
#size of app when opened
spammer.geometry("350x500")
#Title of application
spammer.title("spammerv3")
#Varibles for spamm
clicked = IntVar()
#gui components
title = Label(text="AUTOSPAM V3")
infoentry = Label(text="imput text for spam below")
texttospam = Entry(spammer, background='blue', foreground='red', width=40)
AmountOfTimesSpamedExplainText = Label(text="how many times will this spam")
AmountOfTimesSpamed = OptionMenu(spammer, clicked, "10", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "1000")


SpamDetails = Label(text="If you want to cancel, move mouse to top left of screen", background= 'red', foreground= 'white')
#area that componets apear in
title.grid(row=10,column=0)
infoentry.grid(row=20,column=0)
texttospam.grid(row=30,column=0)
AmountOfTimesSpamedExplainText.grid(row=40,column=0)
AmountOfTimesSpamed.grid(row=50,column=0)

SpamDetails.grid(row=80, column=0)
#code that runs spaming
def StartSpamming():
    texttospam
    time.sleep(2)
    for repeat in range(clicked.get()):
        pyautogui.write(texttospam.get())
        pyautogui.press("enter")
startspaming = Button(text="start spaming (you have two seconds)", command= StartSpamming) 
startspaming.grid(row=70,column=0)

spammer.mainloop()