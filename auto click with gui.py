from datetime import date, datetime
from typing import Tuple
import pyautogui
import time
import tkinter as tk 
import threading  


root = tk.Tk()  
work = False
def click(): 
    time.sleep(0.4)     
    pyautogui.click()
    print("click")
 
def main():
    def run():
        while work == True:
            time.sleep(0.5)     
            #pyautogui.click()
            pyautogui.press('A')
            time.sleep(0.5)
            pyautogui.press('A')
            time.sleep(0.5)
            pyautogui.press('A')
            if work == False:
                break
    thread = threading.Thread(target=run)  
    thread.start()
 
def offsw():
    global work
    work = False
    main()

def onsw():
    global work
    work = True
    main()

def kill():    
 root.destroy()  

##for i in range(3000):
   ## time.sleep(0.1)     
    #pyautogui.click()
   # print("click")

onbutton = tk.Button(root, text = "ON", command = onsw)    
onbutton.pack()    
offbutton =  tk.Button(root, text = "OFF", command = offsw)    
offbutton.pack()
killbutton = tk.Button(root, text = "EXIT", command = kill)    
killbutton.pack()      
        
root.mainloop()  