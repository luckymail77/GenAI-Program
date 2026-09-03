import pyautogui
import time
from datetime import datetime
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

print("Step 1: Opening Chrome browser...")

pyautogui.hotkey('win', 'r')  # Open Run dialog
time.sleep(1)
pyautogui.typewrite('chrome')  # Type 'chrome' to open Google Chrome
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(2)  # Wait for 2 seconds for Chrome to open

print("Step 2: Going to website...")
pyautogui.hotkey('ctrl', 't')  # Open a new tab in Chrome
pyautogui.typewrite('https://www.bing.com/search?EID=MBHSC&form=BGGCMF&pc=W251&DPC=BG00&q=weather+report&PC=U316&FORM=CHROMN')  # Type the website URL
pyautogui.press('enter')  # Press Enter to navigate to the website
time.sleep(2)  # Wait for 2 seconds for the page to load
print("Step 3: Website loaded.")

print ("Step 3: copy the full data of the website...")
pyautogui.hotkey('ctrl', 'a')  # Select all content
pyautogui.hotkey('ctrl', 'c')  # Copy the selected content
time.sleep(1)  # Wait for 1 second

print("Step 4: Open the text editor and paste the content...")
pyautogui.hotkey('win', 'r')  # Open Run dialog
time.sleep(1)
pyautogui.typewrite('notepad')  # Type 'notepad' to open Notepad
pyautogui.press('enter')  # Press Enter to open Notepad
time.sleep(2)  # Wait for 2 seconds for Notepad to open
pyautogui.hotkey('ctrl', 'v')  # Paste the copied content into Notepad
time.sleep(1)  # Wait for 1 second

