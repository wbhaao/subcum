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
print(solution([70, 50, 80, 50], 100))
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