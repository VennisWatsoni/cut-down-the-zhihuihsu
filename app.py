import time
import pyautogui
import judgement
import keyboard
pyautogui.FAILSAFE =False
def ToNext(feet):#9一格
    pyautogui.moveTo(1954,1435, duration=1)#移动到指定位置
    for i in range(feet):
        time.sleep(0.02)
        pyautogui.scroll(-7)

    pyautogui.click(1931,1409)#下条视频位置
    pyautogui.moveTo(196,1099, duration=3)#移动到指定位置
    pyautogui.click(196,1099)#播放按钮
    net=judgement.monitor_net(8,512)
    if net:
        return True
    else:
        return False
    

def SkipTest():
    time.sleep(1.5)
    pyautogui.click(1187,32)#取消测试按钮

def AutoAnswer():
    time.sleep(0.1)
    pyautogui.click(838,888)#b
    pyautogui.click(838,937)
    time.sleep(0.1)
    pyautogui.click(838,787)#a
    pyautogui.click(838,836)
    time.sleep(0.1)
    pyautogui.click(838,989)#c
    pyautogui.click(838,1036)
    time.sleep(0.1)
    pyautogui.click(838,1090)#d
    pyautogui.click(838,1137)
    time.sleep(0.1)
    pyautogui.click(838,1188)#e
    pyautogui.click(1240,1240)#关闭按钮
    pyautogui.moveTo(196,1099, duration=1)#移动到指定位置
    pyautogui.click(196,1099)#播放

def again():
    pyautogui.click(196,1099)#播放按钮
