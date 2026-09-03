import pyautogui
import time

#mouse  operations
pyautogui.moveTo(100, 100, duration=1) # move the mouse to (100, 100) over 1 second
pyautogui.rightClick(100, 100) # right click at (100, 100)
pyautogui.doubleClick(100, 100) # double click at (100, 100)
pyautogui.moveTo(200, 200, duration=1) # move the mouse to (200, 200) over 1 second'
pyautogui.dragTo(300, 300, duration=1) # drag the mouse to (300, 300) over 1 second
pyautogui.scroll(500) # scroll up 500 units
pyautogui.scroll(-500) # scroll down 500 units
