import pyaudio
import numpy as np
import time
import psutil
#检测每秒是否有声音，tm为检测长度、le为最低检测长度
def monitor_video(tm,le):
    vmap5=[0]*tm
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    print("-----开始监测voice------")
    for i in range(0, tm):
        data = stream.read(10240)
        audio_data = np.fromstring(data, dtype=np.short)
        temp = np.max(audio_data)
        vmap5[i]=temp
        vmax5=np.max(vmap5)
        #print(vmax5)
        time.sleep(1)
        if i >= le and vmax5 >= 80:
            print("检测到音频播放")
            print('声阈值:80', vmax5)
            return True 
    print("监测",tm,"S,无音频播放",vmax5)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return False 
#检测视频加载，tm为检测长度、le为最低检测长度
def monitor_net(tm,le):
    nmap5=[0]*tm
    print("-----开始监测netRa------")
    for i in range(tm):
        recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
        time.sleep(1)      
        recv_now = psutil.net_io_counters().bytes_recv
        recv = (recv_now - recv_before)/1024
        nmap5[i]=recv
        nmax5=np.max(nmap5)
        if nmax5 >=le:
            print("加载正常")
            print("阈值:",le,"  网速：","%d"%nmax5)
            return True
    print("未加载")
    print("阈值:",le,"  网速：","%d"%nmax5)
    return False