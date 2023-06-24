import pyautogui

iml = pyautogui.screenshot(region=(600, 450, 700, 500))
iml.save(r".\region.png")
