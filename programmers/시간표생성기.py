import random
from time import *

# 이 알고리즘이 별로 마음에 들진 않지만 완성은 해본다
# 알고리즘 변경을 해보겠다 (못해먹겠음) (대대적이진 않지만..)
subjectList = ["국어","국어","국어","국어",
               "영어","영어","영어","영어",
               "과학","과학","과학","과학",
               "수학","수학","수학","수학",
               "가정","가정","가정",
               "체육","체육","체육",
               "역사","역사",
               "사회","사회",
               "진로",
               "스포",
               "한문",
               "음악",
               "미술"
               ]

# 스케줄
schedules =[]
classNum = 3
# for i in range(classNum-1):
#     schedules.append([["","","","","",""],
#                       ["","","","","",""],
#                       ["","","","","",""],
#                       ["","","","","",""],
#                       ["","","","","",""]])
# shuffle 은 대입이 필요없기에 따로 변수 하나 더 만들기(sorted 이유는 노션 참고)
lst = sorted(subjectList)
w_break = True
# schedules 채우기
for i in range(classNum):
    if w_break == False:
        print("a")
        schedules.append(lst2)
    # while을 계속할것인가
    w_break = True
    # 될때까지
    while w_break:
        random.shuffle(lst)
        # 2차원으로 분할(검사해야해서)
        lst2 = [lst[0:6], lst[6:13], lst[13:19], lst[19:25], lst[25:31]]
        # 검사

        for l in lst2:
            # 하나라도 있으면 안됨
            # 중복이 있는가? 있으면
            # 조건 하나더. 같은시간 같은수업 X
            if len(l) != len(set(l)):
                w_break = True
                break
            # 없으면
            else:
                w_break = False



# 일단 반 중복은 차차해두고 양식에 맞게 출력해야할거같다
# 파일입출력을 통해 시간표를 정리해보자
# 먼저 컴파일러로 출력
schedules.append(lst2)
for c in range(classNum):
    # 교시가 나중에 바뀌는건 가로로 
    # 전부 출력한다음 줄바꿈 할거라서
    for i in range(6):
        for x in range(5):
            print(schedules[c][x][i] ,end=" ") 
        print()
    print("     %s" % (schedules[c][1][6]))
    print()
