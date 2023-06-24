from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # 0.1 second delay before release
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# press q to stop the bot
while keyboard.is_pressed('q') == False:
    # Tile 1 X:  511, Y:  600
    if pyautogui.pixel(511, 600)[0] == 0:
        click(511, 600)
    # Tile 2 X:  618, Y:  600
    if pyautogui.pixel(618, 600)[0] == 0:
        click(618, 600)
    # Tile 3 X:  730, Y:  600
    if pyautogui.pixel(730, 600)[0] == 0:
        click(730, 600)
    # Tile 4 X:  836, Y:  600
    if pyautogui.pixel(836, 600)[0] == 0:
        click(836, 600)

# tile positions may or may not differ
# change it accordingly
