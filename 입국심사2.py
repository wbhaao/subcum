def solution(n, times):
    answer = 0
    # n은 하나 이상이니 한번은 심사를 거쳐야해서 최소값을 정함
    left = min(times) 
    right = max(times) * n
    # 이분탐색 리스트 범위에 하나만 남았을 경우(다음턴에 정지)
    while left <= right:
        mid = (left+ right) // 2
        checked = 0
        for time in times:
            # checked 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            checked += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if checked >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if checked >= n:
            # 같은 경우도 있어 저장
            answer = mid
            # 사람이 더 많으니까. mid보다 적은쪽으로
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif checked < n:
            # 사람이 더 적으니까. mid보다 큰쪽으로
            left = mid + 1
            
    return answer