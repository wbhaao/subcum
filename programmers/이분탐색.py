# 이 문제에 핵심은 결국 이분탐색이다
# 이분탐색은 list가 정렬된 상태에서 진행된다
#  DP를 쓸수 있을거 같다.

N = input()
A = map(int, input().split())
M = input()
B = map(int, input().split())

N = 5
A = [4, 1, 5, 2, 3]
M = 5
B = [1, 3, 7, 9, 5]


A = sorted(A)
B = sorted(B)

mid = -1

for b in B:
    left = mid+1
    right = len(A)-1
    mid = (left+right)//2

    while left <= right:
        mid = (left+right)//2
        if A[mid] == b:
            print(1)
            break
        else:
            if A[mid] > b:
                right = mid-1
            else:
                left = mid+1
    if left > right:
        print(0)