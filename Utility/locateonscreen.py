from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

xpos = 1412 - 998
ypos = 1003 - 906

while 1:
    if pyautogui.locateOnScreen('onemoretime.png', region=(998, 906, xpos, ypos)) != None:
        print("yes")
        time.sleep(0.5)
    else:
        print("no")
        time.sleep(0.5)
