import datetime
import os
import time

path = "/root/auto_restart/"

def check_watt():
    os.system("nvidia-smi > %slog" % path)
    l=[]
    with open(path+"log", 'r') as f:
        l=f.readlines()
    watt = int(l[9].split('W /')[0].split(' ')[-1])
    if watt < 100:
        return True
    else:
        return False

def restart():
    if check_free():
        os.system("miner restart")
        print("restart", datetime.datetime.now())
    if check_watt():
        time.sleep(300)
        if check_watt():
            os.system("miner restart")
            print ("restart", datetime.datetime.now())




def check_free():
    os.system("free -h > %slog1" % path)
    content=''
    with open(path+"log1", 'r') as f:
        content=f.read()
    l1 = content.split('\n')[1].split(' ')
    target = list(filter(lambda x: x != '', l1))[3]
    if "Mi" in target and int(target.strip("Mi")) < 50:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        restart()
        time.sleep(60) 
