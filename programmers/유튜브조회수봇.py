from grpc import channel_ready_future
import pyautogui
import time
import sys
import random

SLEEP_TIME = 2.2

ID = "glistabc"
PASSWORD = "goo!1052"
CHANNEL_LINK = "https://www.youtube.com/channel/UCk9By_MVaba4LDKCFwp9cCA/videos"

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()
import pyperclip

def my_write(text):
    pyperclip.copy(text)
    time.sleep(SLEEP_TIME/5)
    pyautogui.hotkey("ctrl", "v")

# 크롬 선택
for id_ in range(1,3):
    id_ = ID+str(id_)
    my_click("chrome.png", 10)
    time.sleep(SLEEP_TIME*1.5)

    pyautogui.hotkey("ctrl", "shift", "n")
    # 유튜브 들어가기
    my_write("https://www.youtube.com/")
    pyautogui.press("enter")
    # 로그인 버튼 누르기
    my_click("asset2/login.png", timeout=30)
    time.sleep(SLEEP_TIME)
    # ID 입력
    my_write(id_)
    time.sleep(SLEEP_TIME)
    pyautogui.press("enter")
    time.sleep(SLEEP_TIME+1)
    # PASSWORD 입력
    my_write(PASSWORD)
    time.sleep(SLEEP_TIME)
    pyautogui.press("enter")
    time.sleep(SLEEP_TIME+2)

    pyautogui.moveTo(209,50)
    pyautogui.click()
    time.sleep(SLEEP_TIME-1.5)

    my_write(CHANNEL_LINK)
    pyautogui.press("enter")
    time.sleep(SLEEP_TIME)
    my_click("asset2/subscribe.png", timeout=30)
    time.sleep(SLEEP_TIME-2)

    pyautogui.hotkey("alt", "f4")