import pyautogui
print('Ctrl+Cを押すと終了します')
try:
    while True:
        print("start")
        pyautogui.click(x=200,y=400)
        pyautogui.press("up")
        pyautogui.press("enter")
        pyautogui.click(x=200,y=800)
        pyautogui.press("up")
        pyautogui.press("enter")
        pyautogui.click(x=800,y=400)
        pyautogui.press("up")
        pyautogui.press("enter")
        pyautogui.click(x=800,y=800)
        pyautogui.press("up")
        pyautogui.press("enter")
        pyautogui.click(x=1400,y=400)
        pyautogui.press("up")
        pyautogui.press("enter")
        pyautogui.click(x=1400,y=800)
        pyautogui.press("up")
        pyautogui.press("enter")
        print("during")
        pyautogui.sleep(20)
        pyautogui.click(x=200,y=400)
        pyautogui.hotkey("ctrlleft","c")
        pyautogui.click(x=200,y=800)
        pyautogui.hotkey("ctrlleft","c")
        pyautogui.click(x=800,y=400)
        pyautogui.hotkey("ctrlleft","c")
        pyautogui.click(x=800,y=800)
        pyautogui.hotkey("ctrlleft","c")
        pyautogui.click(x=1400,y=400)
        pyautogui.hotkey("ctrlleft","c")
        pyautogui.click(x=1400,y=800)
        pyautogui.hotkey("ctrlleft","c")
        print("end")
        pyautogui.sleep(10)
except KeyboardInterrupt:
    print('\n終了')



# x300 y730
# x900 y800
#x1600 y800


#x200 y400
#x200 y800
#x800 y400
#x800 y800
#1400 y400
#x1400 y800