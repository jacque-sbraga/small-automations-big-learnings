import pyautogui

mouse_init = (769, 1060)

edge_icon_position = (642,320)

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)


def search(text):
    pyautogui.typewrite(text)
    pyautogui.press('return')

if __name__ == '__main__':
    pyautogui.sleep(2)
    click(*mouse_init)

    pyautogui.sleep(2)

    click(*edge_icon_position)

    pyautogui.sleep(2)

    search('https://www.google.com/')

    pyautogui.sleep(2)

    search('dolar hoje')

    pyautogui.sleep(2)


