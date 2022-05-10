# x = int(input())
# num_list = []

# num = 0
# num_count = 0

# while num_count < x:
#     num += 1
#     num_count += num

# num_count -= num

# if num % 2 == 0:
#     i = x - num_count
#     j = num - i + 1
# else:
#     i = num - (x - num_count) + 1
#     j = x - num_count

# print(f"{i}/{j}")

# 오븐 시계

# hour, min = map(int, input().split())
# time_ = int(input())

# # 시간 추가
# min += time_
# # min이 60분 초과시 1시간 +
# hour += min // 60
# min %= 60
# hour %= 24
# print(f"{hour} {min}")

# dices = list(map(int, input().split()))

# lst = [dices.count(dices[0]), dices.count(dices[1])]
# if lst[0] == 3:
#     print(10000+dices[0]*1000)
# elif max(lst) == 2:
#     print(1000+dices[lst.index(max(lst))]*100)
# else:
#     print(max(dices)*100)




lock = [0]
# and
#lock에 0이 존재하지 않는지?
# 하나라도 False면 False
# if all(0 != l for l in lock):
#     # return True
#     pass
# # or
# #lock에 0이 하나라도 존재하는지?
# # 하나라도 True면 True
# if any(0 == l for l in lock):
#         #return True
#     pass

def solution(people, limit):
    cnt = 0
    people.sort()
    while len(people) > 1:
        cnt += 1
        # 내보낼 수 있다
        if people[0]+people[-1] <= limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
    answer = len(people) + cnt
    return answer
# print(solution([70, 50, 80, 50], 100))
########################################
def solution(people, limit):
    answer = 0
    people.sort()
    # f:front
    # e:end
    f_cnt =0
    e_cnt =len(people)-1 # index니까 -1
    while e_cnt - f_cnt >= 1: # 같은 수 => 탈출
        # 가장 작은 수 + 가장 큰 수 <= limit
        if people[f_cnt] + people[e_cnt] <= limit:
            # f와 end 전부 삭제 처리 (좌표 앞으로)
            f_cnt += 1
            e_cnt -= 1
        else:
            # 아니면 뒷수만 삭제 처리
            e_cnt -= 1
        answer += 1
    # 수 하나가 남았을 경우 (없을 경우 f와 e가 교차됨)
    if e_cnt == f_cnt:
        answer += 1
    return answer

def solution(s):
    cnt_dict = {}
    s = s[1:-1]
    lst = s.split("}")[:-1]
    for i in range(len(lst)):
        lst[i] = lst[i].replace("{","")
        if not (lst[i][0] in list(map(str, range(0,10)))):
            lst[i] = lst[i][1:]
        for x in lst[i].split(","):
            if cnt_dict.get(x) == None:
                cnt_dict[x] = 1
            else:
                cnt_dict[x] += 1
    from operator import itemgetter
    answer_temp = sorted(cnt_dict.items(), key=itemgetter(1), reverse=True)
    answer = []
    for a in answer_temp:
        answer.append(a[0])
    return list(map(int, answer))

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

def solution(s):
    answer = []
    # 양끝'{', '}' 제거 // },{ 로 문자열 나누기
    s1 = s.lstrip('{').rstrip('}').split('},{')
    new_s = []
    for i in s1:
        # ,으로 문자열 나눠서 숫자 개별로 넣기(list로 넣음)
        new_s.append(i.split(','))
    # 길이가 짫은순대로 정렬 (list에 하나가 있으면 
    # 제일 많이 들어가있고 2개가 들어가있으면 
    # 그중 1번째,2번째가 들어가있다)
    new_s.sort(key = len)
    for i in new_s:
        for j in range(len(i)):
            # 이미 포함되있으면 안포함시킴(순차적으로 append)
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))