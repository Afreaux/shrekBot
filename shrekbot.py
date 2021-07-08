import pyautogui, time
time.sleep(10)
f = open("shrek", "r")

...
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(6)
...

