import pyautogui
import time
import sys
pyautogui.FAILSAFE=False


def attack(fp,if_center=True,change=(0,0),wait_time_max=5):
    time_start=time.time()
    while True:
        time_new=time.time()
        location = pyautogui.locateOnScreen(fp)
        if location != None:
            left, top, width, height = location
            if if_center==True:
                pyautogui.click(left + int(width / 2), top + int(height / 2))
                break
            else:
                pyautogui.click(left + change[0], top + change[1])
                break
        if time_new-time_start>=wait_time_max:
            return 'error'
    return 'success'

def zzuli_wifi():
    answer=attack(fp='zzuli_wifi1.png')
    if answer!='success':
        answer=attack(fp='zzuli_wifi2.png')
        if answer != 'success':
            answer=attack(fp='zzuli_wifi3.png')
            if answer != 'success':
                answer=attack(fp='zzuli_wifi4.png')
    return

def start():
    attack(fp='wifi_no_link.png')
    zzuli_wifi()
    attack(fp='zzuli_wifi_link2.png')
    attack(fp='choose_web.png')
    attack(fp='choose_liantong.png',if_center=False,change=(68,81))
    attack(fp='login.png')
    attack(fp='close.png')

start()
sys.exit()
