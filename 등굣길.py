# 시작부터 잘못됐다!
def solution(m, n, puddles):
    lst = [[1, 1]]
    
    
    while True:
        # 앞에 물웅덩이와 벽이 없으면
        for i in range()
        if lst[0][0]+1 > m or \
          [lst[0][0]+1, lst[0][1]] == puddles:
            pass
        else:
            lst.append([lst[0][0]+1, lst[0][1]])
        # 앞에 물웅덩이와 벽이 없으면
        if lst[0][1]+1 > n or \
          [lst[0][0], lst[0][1]+1] == puddles:
            pass
        else:
            lst.append([lst[0][0], lst[0][1]]+1)
        del lst[0]
    answer = 0
    return answer