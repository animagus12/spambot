import pyautogui, time
time.sleep(5)
f=open("script1", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

