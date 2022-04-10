# 시작부터 잘못됐다!
from collections import deque

def solution(m, n, puddles):
    lst = deque([[1, 1]])
    cnt = 0
    
    while lst:
        # 앞에 물웅덩이와 벽이 없으면
        if lst[0] == [m,n]:
            cnt += 1
        else:
            # 앞에 물웅덩이와 벽이 없으면 (가로 전진)
            if lst[0][0]+1 <= m and \
               not ([lst[0][0]+1, lst[0][1]] in puddles):
                lst.append([lst[0][0]+1, lst[0][1]])
            # 앞에 물웅덩이와 벽이 없으면 (세로 전진)
            if lst[0][1]+1 <= n and \
               not ([lst[0][0], lst[0][1]+1] in puddles):
                lst.append([lst[0][0], lst[0][1]+1])
                
        lst.popleft()
    return cnt % 1000000007

print(solution(4, 3, [[2, 2]]))