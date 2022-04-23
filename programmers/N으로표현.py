# from ast import operator


# def solution(N, number):
    
#     # 최대 N이 들어갈수 있는 개수는 8이다
#     for i in range(1, 9):
#         operator_ = []
#         # N 사이에 들어갈 연산자 개수를 정함
#         for x in range(1, i): # i-1만큼 들어갈 수 있다
#             for o in ["","+","-","*","//"]:
#                 # 여기서 어디에 넣을지 고르기

#     answer = 0
#     return answer

def solution(N, number):
    S = [{N}]
    if N == number:
        return 1
    # 2부터 8까지 N이 들어가는거(하나 들어갈건 이미 위에서 처리)
    for i in range(2, 9):
        # i번만큼 N을 늘림 ex. N=2, i=4라면 NNNN, 2222 int속성
        lst = [int(str(N)*i)]
        # X_i는 연산기호의 숫자
        for X_i in range(0, int(i / 2)):
            # S의 X_i번째 인덱스를 x안에 넣음 // dict라 2번 돔
            for x in S[X_i]:
                # 
                for y in S[i - (X_i + 2)]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    # 0을 나누면 ZeroDivision 에러가 나서 if문
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        # lst에 num와 같은게 있다면 i return
        if number in set(lst):
            return i
        # 없다면 S에 lst 추가
        S.append(lst)
    return -1
    