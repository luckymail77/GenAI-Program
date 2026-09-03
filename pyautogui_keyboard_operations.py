'''
import pyautogui
import time

# keyboard operations
pyautogui.press('enter') # press the enter key
time.sleep(1) # wait for 1 second
pyautogui.press('space') # press the space key
time.sleep(1) # wait for 1 second
pyautogui.press('backspace') # press the backspace key
time.sleep(1) # wait for 1 second
pyautogui.typewrite('Hello, World!') # type the text 'Hello, World!'
time.sleep(1) # wait for 1 second
'''

import pyautogui

screenshot = pyautogui.screenshot() # take a screenshot
screenshot.save('final.png') # save the screenshot as 'final.png'



