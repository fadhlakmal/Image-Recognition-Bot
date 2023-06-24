from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# press q to stop
while keyboard.is_pressed('q') == False:
    flag = 0
    # my region is (600, 450, 700, 500)
    # may or may not differ, change accordingly
    pic = pyautogui.screenshot(region=(600, 450, 700, 500))

    width, height = pic.size

    # Check every 5 pixels within the region
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            
            r, g, b = pic.getpixel((x, y))
            
            # Target center RGB: (255, 219, 195)
            if r == 255 and g == 219 and b == 195:
                click(x + 600, y + 450)
                time.sleep(0.05)
                flag = 1
                break
            
        if flag == 1:
            break
            
