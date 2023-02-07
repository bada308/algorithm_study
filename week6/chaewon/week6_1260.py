# BJ 1260 / SILVER II /

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
