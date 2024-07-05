import pyautogui

option = pyautogui.confirm('Click the desired button', buttons=['Excel', 'Word', 'Notepad'])

def hotkey(*keys):
    pyautogui.hotkey(*keys)

def typeText(text, interval=0):
    pyautogui.typewrite(text, interval)
    pyautogui.press('enter')

close_window = lambda: pyautogui.getActiveWindow().close()
win_r = ('win', 'r')

if option == 'Excel':
    hotkey(*win_r)
    typeText('excel', 0.1)

elif option == 'Word':
    hotkey(*win_r)
    typeText('winword', 0.1)

else:
    hotkey(*win_r)
    typeText('notepad', 0.1)
