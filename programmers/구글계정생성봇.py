import pyautogui
import time
import sys
import random

SLEEP_TIME = 2.2

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
    time.sleep(SLEEP_TIME/3)
    pyautogui.hotkey("ctrl", "v")

def random_Name():
    name = (random.randint(0, 15)*588)+(random.randint(0, 20)*28)+random.randint(0, 27)+44032
    return chr(name)

# 크롬 선택
my_click("asset/chrome.png", 10)
time.sleep(SLEEP_TIME*1.5)
# 링크 입력
my_write("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME*2.2)
# 성 입력
my_write(random_Name())
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME)
# 이름 입력
my_write(random_Name())
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME)
# 아이디 입력
my_write("glistABC2")
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME)
# 비번 입력
my_write("goo!1052")
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME)
# 비번 재확인
my_write("goo!1052")
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME)

# 확인
pyautogui.moveTo(493, 542)
pyautogui.click()
time.sleep(SLEEP_TIME*1.5)
# 전번 찍기
my_write("01031620504")
pyautogui.hotkey("enter")
time.sleep(SLEEP_TIME*20)

# 여기에 확인문자 받는 텀이 있어야함

# 복구 이메일
pyautogui.moveTo(440, 520)
pyautogui.click()
my_write("a31620504@gmail.com")
time.sleep(SLEEP_TIME)
# 년도
pyautogui.moveTo(365,605)
pyautogui.click()
my_write("2000")
time.sleep(SLEEP_TIME)
# 월
pyautogui.moveTo(477, 598)
pyautogui.click()
time.sleep(SLEEP_TIME)
my_click("asset/May.png", 10)
pyautogui.click()
time.sleep(SLEEP_TIME)
# 일
pyautogui.moveTo(603, 606)
pyautogui.click()
my_write("1")
time.sleep(SLEEP_TIME)
# 성별
pyautogui.moveTo(462,690)
pyautogui.click()
time.sleep(SLEEP_TIME)
my_click("asset/male.png", 10)
pyautogui.click()
time.sleep(SLEEP_TIME*1.5)

my_click("asset/next.png", 10)
time.sleep(SLEEP_TIME*1.5)

my_click("asset/skip.png", 10)
time.sleep(SLEEP_TIME*1.5)

pyautogui.moveTo(1273,268)
pyautogui.dragTo(1271,947)
time.sleep(SLEEP_TIME)
my_click("asset/checkBox.png", 10)
time.sleep(SLEEP_TIME)
my_click("asset/checkBox.png", 10)
time.sleep(SLEEP_TIME)
my_click("asset/createAccount.png", 10)