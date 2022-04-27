# from time import *
# from keyboard import *

# # 0:하늘
# # 1:땅
# # 2:공룡
# # 3:선인장
# # 4:구름
# blockList = ["🟦","🟩","🟨","🟥","⬜️"]

# display = [[0,0,0,0,0, 0,0,0,0,0],
#            [0,0,0,0,0, 0,0,0,0,0],
#            [0,0,2,0,0, 0,0,0,0,0],
#            [0,0,2,0,0, 0,0,0,0,0],
#            [1,1,1,1,1, 1,1,1,1,1],]

# def printDisplay():
#     for dis in display:
#         for d in dis:
#             print(blockList[d], end="")
#         print()

# while True:
#     if read_key() == "space":
#         print('hlelo')
#         break
#     # 선인장이 없으면
#     if not any(3 in l for l in display):
#         display[3][9] = 3
#     # 선인장이 있으면
#     else:
#         cactusIndex = display[3].index(3)
#         display[3][cactusIndex] = 0
#         # 넘으면 추가하지 않고 삭제만 함(그러면 위에 if에 걸림)
#         if cactusIndex-1 > -1:
#             display[3][cactusIndex-1] = 3
#     printDisplay()
#     sleep(0.5)

def solution(s):
    lst = list(map(int, s.split(" ")))
    return "%d %d" % (min(lst), max(lst))

def solution(priorities, location):
    cnt = 1
    priorities_dict = {} # temp는 무슨역할?

    for index, p in enumerate(priorities): # 인덱스를 지정해줘서 loca와 index가 같으면 return
        priorities_dict[index] = p 
    # key : 인덱스 , value : 값, priorities : 값
    while True:
        # 첫번째가 priorities_dict 중 우선도가 가장 높나?
        if next(iter(priorities_dict.values())) == max(priorities_dict.values()): 
            # 나의 인덱스와 구하고자 하는 index가 같나
            if next(iter(priorities_dict.keys())) == location:
                return cnt
            # 다르면 삭제
            del priorities_dict[next(iter(priorities_dict.keys()))] 
            cnt += 1 
        else: # 해석 : 맨앞에껄 맨뒤로 옮기는 것
            # key와 value를 저장하고 마지막에 index에 append
            temp_key = next(iter(priorities_dict)) # 삭제하는 key 저장
            temp_value = priorities_dict[next(iter(priorities_dict))] # 삭제하는 value 저장
            del priorities_dict[next(iter(priorities_dict.keys()))] # 첫번째 순서 삭제
            # 첫번쨰 값 append
            priorities_dict[temp_key] = temp_value    