import time
import pyautogui
import judgement
import keyboard
pyautogui.FAILSAFE =False
#通过切换到下一个视频，feet为一格目录的长度
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
    
#跳过章节测试题目
def SkipTest():
    time.sleep(1.5)
    pyautogui.click(1187,32)#取消测试按钮
#自动填写ai题目，abcde为单个选项位置
def AutoAnswer():
    time.sleep(0.5)
    ae=787
    while ae<=1188:
        time.sleep(0.01)
        pyautogui.click(838,ae)#a
        ae+=17
    #pyautogui.click(838,888)#b
    #pyautogui.click(838,937)
    #time.sleep(0.1)
    #pyautogui.click(838,787)#a
    #pyautogui.click(838,836)
    #time.sleep(0.1)
    #pyautogui.click(838,989)#c
    #pyautogui.click(838,1036)
    #time.sleep(0.1)
    #pyautogui.click(838,1090)#d
    #pyautogui.click(838,1137)
    #time.sleep(0.1)
    #pyautogui.click(838,1188)#e
    #避免全部取消
    pyautogui.click(838,787)#a
    pyautogui.click(838,1036)#c

    pyautogui.click(1240,1240)#关闭按钮
    pyautogui.moveTo(196,1099, duration=1)#移动到指定位置
    pyautogui.click(196,1099)#播放

def again():
    pyautogui.click(196,1099)#播放按钮
