# BJ 1260 / SILVER II / 164ms

import sys
from collections import deque

n, m, v = map(int, input().split(' '))


# 인접 행렬 생성 : 5 by 5 이차원 리스트 생성
graph = [[0] * (n + 1) for _ in range(n + 1)]           # n + 1인 이유 : n의 범위가 1부터이기 때문에, 노드값이 0인 노드가 존재X = 인덱스가 0인 graph값을 0으로 남겨두어야 함

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    graph[a][b] = 1                 # 두 노드를 연결하는 엣지는 양방향
    graph[b][a] = 1

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)


def dfs(v):
    dfs_visited[v] = 1                  # 시작 노드 v를 방문 -> visited 값을 1로 변경
    print(v, end=' ')

    for i in range(1, n + 1):
        if (not dfs_visited[i]) and graph[v][i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    bfs_visited[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for j in range(1, n + 1):
            if (not bfs_visited[j]) and graph[v][j]:
                queue.append(j)
                bfs_visited[j] = 1


dfs(v)
print()
bfs(v)


'''
NOTE:
DFS, BFS의 가장 기본 문제인 것 같다
기본 개념과 예제 코드까지 다 익히고 나서 문제를 푼건데도 어려웠다
예제에서는 graph를 처음부터 인접 리스트로 저장해뒀었는데
여기서는 입력 받고 인접 행렬 또는 인접 리스트로 직접 바꿔 저장하는 부분을 구현하는 게 어려웠다 ㅠ

인접 리스트를 구현하는 코드는 아래와 같다

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

파이팅...
'''