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


def solution(n, times):
    answer = 0
    # n이 가장 길게 걸리는 사람에게 받을 때
    # times[-1] * n : 최대로 걸릴수 있는 시간 
    # (time이 정렬되있나?)
    # 생각해보니 [-1]보다 min()이 더 좋다. 왜냐면 
    # 최대값 계산에서 최소값을 찾고 거기에만 계산했을때가
    # 가장 낮은 최대값이고 가장 간단히 구할수 있음
    # 더 큰값은 서브라 생각하고 계산하면 됨 
    start, end, mid = 1, min(times) * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        # mid 는 최소값일껄?
        for time in times:
            # mid 시간 동안 할수있는 계산 보기 
            total += mid // time
        # 만약 할수있는계산이 n보다 많다!(시간이 남는다)
        # 같아도 더 적을수 있는게 왼쪽이 있을수 있으니까
        if total >= n:
            # 왼쪽(더 작은쪽)으로 감
            end = mid
        # 만약 할수있는계산이 n보다 적다!(시간이 적다)
        # 정답을 놓치더라도 start가 한칸씩 앞으로 가서 정답에 도착
        else:
            # 오른쪽(더 큰쪽)으로 감
            start = mid + 1
    answer = start
    return answer