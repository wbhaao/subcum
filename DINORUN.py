from time import *
from keyboard import *

# 0:하늘
# 1:땅
# 2:공룡
# 3:선인장
# 4:구름
blockList = ["🟦","🟩","🟨","🟥","⬜️"]

display = [[0,0,0,0,0, 0,0,0,0,0],
           [0,0,0,0,0, 0,0,0,0,0],
           [0,0,2,0,0, 0,0,0,0,0],
           [0,0,2,0,0, 0,0,0,0,0],
           [1,1,1,1,1, 1,1,1,1,1],]

def printDisplay():
    for dis in display:
        for d in dis:
            print(blockList[d], end="")
        print()

while True:
    if read_key() == "space":
        print('hlelo')
        break
    # 선인장이 없으면
    if not any(3 in l for l in display):
        display[3][9] = 3
    # 선인장이 있으면
    else:
        cactusIndex = display[3].index(3)
        display[3][cactusIndex] = 0
        # 넘으면 추가하지 않고 삭제만 함(그러면 위에 if에 걸림)
        if cactusIndex-1 > -1:
            display[3][cactusIndex-1] = 3
    printDisplay()
    sleep(0.5)