import pyautogui
import time
time.sleep(0.5)
for repeat in range(1000):
     pyautogui.write("hello")
     pyautogui.press('enter')