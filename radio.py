#!/usr/bin/env python3
import multiprocessing
import time
import urllib.request
import os

urlStream   =   "https://ice.creacast.com/radio"
now         =   time.localtime()
mp3File     =   "/home/pi/radio-"+time.strftime("%Y-%m-%d", now)+".mp3"
duree       =   60 * 20

# # # # # # # # # # # # # # # #

def download(url, file):
    urllib.request.urlretrieve(url, file)
    '''for i in range(100):
        print(url)
        print(file)
        print("Tick-"+str(i))
        time.sleep(1) '''

if __name__ == '__main__':
    p = multiprocessing.Process(target=download, name="DL", args=(urlStream, mp3File, ))
    p.start()
    time.sleep(duree)
    if p.is_alive():
        p.terminate()
        #p.kill()
        p.join()

os.system("chmod 666 "+mp3File)
# fin
