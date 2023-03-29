import pyautogui
import time

# write me a pyautogui script that will press the down arrow 25 times with a delay of 0.2 seconds between each press and delay of 3 seconds between each set of 25 presses

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

time.sleep(5)
for i in range(12):
    for i in range(25):
        pyautogui.press('down')
        print(i)
        if i == 24:
            pyautogui.sleep(3)
            i = 0
