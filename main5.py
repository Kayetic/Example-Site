import pyautogui
import time

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

for i in range(1, 26):
    pyautogui.press('down')
    if i == 25:
        time.sleep(3)
        i = 0
