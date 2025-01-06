import pygetwindow
import pyautogui
from time import sleep

while 1: 
        active_window = pygetwindow.getActiveWindow()
        if active_window:
                left, top = active_window.left, active_window.top
                active_window.restore()
                active_window.moveTo(left - 10, top)
        sleep(0.1)
