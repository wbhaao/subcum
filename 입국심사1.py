# def multfly(x):
#     return x * 2

# def solution(n, times):
#     answer = 0
#     # 이걸로 첫번째 턴 손님은 다 끝남
#     n -= len(times)
#     # 다음에 할때 마칠 시간
#     times_temp = list(map(multfly, times))
#     while n > 0:
#         n -= 1
#         minIndex = times_temp.index(min(times_temp))
#         # 한명 들어갈때마다 += times[minIndex]
#         answer = times_temp[minIndex]
#         times_temp[minIndex] += times[minIndex]
        
#     return answer

# print(solution(6, [7, 10]))