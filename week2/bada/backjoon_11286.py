'''
/* 문제 정보 */
11286번 - 절댓값 힙
난이도 - 실버 1
알고리즘 분류 : 자료구조, 우선순위 큐

/* 풀이 방법 */

-> heapq(우선순위 큐) 모듈 사용, 나중에 heapq 구현하기!

1. 변수&container 선언, 입력
2.1. N번 반복하며 숫자 입력
2.2 x가 0이 아닐 때 : 튜플 형태로 (x의 절댓값, x) heap에 push -> 튜플 형태로 입력시 0번 인덱스 값으로 정렬, 동일하면 1번 인덱스 ...
2.3 x가 0이면 heappop을 이용해 절댓값이 가장 작은 x 출력하고 heap이 비어있으면 0 출력

'''
import sys
import heapq

# 1
N = int(input())
heap = []

# 2

for _ in range(N):
    num = int(sys.stdin.readline())
    if(num != 0):
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)



'''
/* 오답노트 */
- heap 사용법
- 수행시간 줄여주는 입력
input() 대신 sys.stdin.readline()

/* 느낀점 */
- 스택이 아니라 우선순위 큐가 나오니까 또 어렵다
- 파이썬 모듈 참 잘 되어 있다, 하지만 직접 구현해야 완벽히 이해할 수 있을 것 같다.
'''