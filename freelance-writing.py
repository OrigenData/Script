#script freelance writing on python

import pyautogui
import time 
time.sleep(5)

for i in range(100):
    pyautogui.typewrite(str(i))
    pyautogui.typewrite("\n")
    time.sleep(5)
    
# dnf install scrot
# pip install PyAutoGUI
