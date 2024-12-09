import judgement
import app
import keyboard
import os

global mv
def stop ():
    
    global st
    st=0  
st=1
mv='showing'

while (st):
    keyboard.add_hotkey('esc', stop)
    if st==0:
        print("程序退出")
        break
    mov=judgement.monitor_video(20,5)           
    if  mov :
        print('the movie is')
        print(mv)
    elif not mov and mv=='showing':
        app.again()
        print("点击开关")
        mov=judgement.monitor_video(5,0)
        if not mov:
            app.again()
            print("点击开关")
            mov=judgement.monitor_video(5,0)
            if not mov:
                app.AutoAnswer()
                mv='OverAnswer'
                print(mv)
    
    else:
        nex=app.ToNext(9)
        fr=0
        while not nex :
            app.SkipTest()
            nex=app.ToNext(10)
            fr+=1
            if fr>=3:
                nex=True
        print("尝试跳过空白")
        mv='showing'
        L=0
    
    
    
    
    
