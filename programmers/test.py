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
if all(0 != l for l in lock):
    # return True
    pass
# or
#lock에 0이 하나라도 존재하는지?
# 하나라도 True면 True
if any(0 == l for l in lock):
        #return True
    pass



