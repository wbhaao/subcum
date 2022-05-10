from random import *
from time import *

# 이 알고리즘이 별로 마음에 들진 않지만 완성은 해본다
# 알고리즘 변경을 해보겠다 (못해먹겠음) (대대적이진 않지만..)
subjectList4 = ["국어","영어","과학","수학"]
subjectList3 = ["가정","체육"]
subjectList2 = ["사회","역사"]
subjectList1 = ["진로","스포츠","한문","음악","미술"]

subjectList_temp = sorted(subjectList)
classNum = int(input("반 개수:"))
# 스케줄
schedules =[[["","","","","",""],
             ["","","","","",""],
             ["","","","","",""],
             ["","","","","",""],#곱하면 버그생김
             ["","","","","",""]]]
for i in range(classNum-1):
    schedules.append([["","","","","",""],
                      ["","","","","",""],
                      ["","","","","",""],
                      ["","","","","",""],
                      ["","","","","",""]])
cnt = 0
sevenSchools = []
# 랜덤으로 하면 계속 안되는 경우가 발생한다
# 조건에 적은 과목은 하루에 2~3개 이하로 들어가게 하기
# 조건으로 채워넣기
for schI, sch in enumerate(schedules): # 6 * 5짜리 시간표 classNum개
    for scI, sc in enumerate(sch): # 6칸 시간표 5개
        for sI, s in enumerate(sc): # 과목 하나
            cnt += 1
            print(cnt)
            # 조건에 다 충족할때까지
            while True:
                print("%d, %d, %d" % (schI, scI, sI))
                sleep(0.1)
                subject = subjectList_temp[0]
                print(subject)
                print(len(subjectList_temp))
                # 조건 달기
                # 하루에 같은 과목 X
                if subject in sc: 
                    # 다음 반복으로 스킵
                    continue
                # 같은 시간 같은 수업을 받는 반 X
                for i in range(classNum):
                    # sch의 schedules에서의 인덱스를 넣어주어야 한다
                    if subject == schedules[i][scI][sI] and schI != i:
                        # 다음 반복으로 스킵
                        continue
                # 조건에 전부 만족한다면
                subjectList_temp.remove(subject)
                # print(subjectList_temp)
                schedules[schI][scI][sI] = subject
                break
    # 하나가 남을텐데 그건 7교시로 넘기기
    sevenSchools.append(subjectList_temp[0])
    # 옆반으로 넘어가서 초기화
    subjectList_temp = sorted(subjectList)
    
print(schedules)