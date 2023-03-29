import pyautogui
import time

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

for i in range(12):
    for j in range(25):
        pyautogui.press('down')
    time.sleep(3)
