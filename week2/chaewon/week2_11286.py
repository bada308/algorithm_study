import sys, heapq

n = int(sys.stdin.readline())
q = []
result = []

'''
아이디어 : 입력받은 x값을 (x 절댓값, x값)의 튜플 형태로 힙에 저장

** 튜플 값을 힙에 저장하면, 튜플의 첫 번째 원소값을 기준으로 힙 구성
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & return
'''


for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x != 0:                              # 입력값이 0이 아니면
        heapq.heappush(q, (abs(x), x))      # 힙 q에 (x절대값, x) 튜플을 삽입

    else:                   # 입력값이 0이면
        if not q:                   # q가 비어 있으면
            result.append(0)        # result에 0 추가

        else:                                       # q가 비어 있지 않으면
            result.append(heapq.heappop(q)[1])      # 힙 내에서 절대값이 가장 작은 원소 삭제 & 그 x값을 result에 추가

print(*result, sep='\n')