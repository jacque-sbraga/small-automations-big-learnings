import pyautogui

def hotkey(*keys):
    pyautogui.hotkey(*keys)

def typeText(text, interval=0):
    pyautogui.typewrite(text, interval)
    pyautogui.press('enter')

close_window = lambda: pyautogui.getActiveWindow().close()

hotkey('win', 'r')

pyautogui.sleep(2)

typeText('notepad')

pyautogui.sleep(2)
typeText('Opening Notepad using PyAutoGUI', 0.1)

pyautogui.sleep(2)
hotkey('ctrlleft', 's')

pyautogui.sleep(2)

typeText('created using pyautogui', 0.1)

hotkey('enter')
close_window()





