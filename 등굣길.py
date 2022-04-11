# 시작부터 잘못됐다!
# 지금 해석할거
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

# 해석용
def solution(m, n, puddles):
    # 왜 거꾸로 할까..
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    # dp는 
    dp = [[0] * (m + 1) for _ in range(n + 1)]  
    dp[1][1] = 1          

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]