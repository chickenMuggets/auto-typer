from tkinter import *
import pyautogui
import time
spammer = Tk()
pyautogui.FAILSAFE = TRUE
#size of app when opened
spammer.geometry("350x500")
#Title of application
spammer.title("spammerv2 (NOW WITH GUI!)")
#Varibles for spamm
clicked = IntVar()
clicked.set("Click here to select")
#code that runs spaming
def StartSpamming():
    texttospam
    time.sleep(2)
    for repeat in range(999999999999999999999999999999999999):
        pyautogui.write(texttospam.get(), .01)
        pyautogui.press("enter")
        pyautogui.sleep(0.1)
#gui components
title = Label(text="AUTOSPAM V2")
infoentry = Label(text="imput text for spam below")
texttospam = Entry(spammer, bg='blue', fg='red', width=40)
AmountOfTimesSpamedExplainText = Label(text="how many times will this spam")
AmountOfTimesSpamed = OptionMenu(spammer, clicked, "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "1000")
startspaming = Button(text="start spaming (you have two seconds)", command=StartSpamming) 
SpamDetails = Label(text="If you want to cancel, move mouse to top left of screen", bg = 'red', fg= 'white')
#area that componets apear in
title.grid(row=10,column=0)
infoentry.grid(row=20,column=0)
texttospam.grid(row=30,column=0)
AmountOfTimesSpamedExplainText.grid(row=40,column=0)
AmountOfTimesSpamed.grid(row=50,column=0)
startspaming.grid(row=70,column=0)
SpamDetails.grid(row=80, column=0)
spammer.mainloop()