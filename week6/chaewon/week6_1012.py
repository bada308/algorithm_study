# BJ 1012 / SILVER II / 72ms

import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(sys.stdin.readline().strip())


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]          # 행
            ny = y + dy[i]          # 열
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return 0


for _ in range(t):
    cnt = 0
    n, m, k = map(int, sys.stdin.readline().strip().split(' '))
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        graph[x][y] = 1

        # 2차원 리스트를 보기 좋게 출력하는 코드
    # for i in graph:
    #     for j in i:
    #         print(j, end=" ")
    #     print()

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1

    print(cnt)


'''
NOTE:

핵심 아이디어가 인접한 1을 0으로 모두 바꾸어주는 건데
아예 생각지도 못했다 ...

즉, graph[x][y] = 1일 때, 해당 위치에서 인접한 1을 모두 0으로 바꾸어 주는 bfs를 실행한다.
이때 bfs는, x와 y에서 상하좌우로 인접한 1 뿐만 아니라, x와 y에서 상하좌우로 이동한 좌표 nx, ny에서 인접한 1 까지 0으로 변경해준다.
이 과정을 인접한 1이 없을 때까지 반복한다.

이 아이디어를 떠올리는 것이 핵심이었는데
문제를 많이 안풀어봐서 그런가 생각을 못해냈다 ㅠ

'''