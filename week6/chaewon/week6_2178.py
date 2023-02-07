# BJ 2178 / SILVER I / 76ms

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(' '))

graph = [[0] for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    cnt = 1
    queue = deque()
    queue.append((0, 0, cnt))
    visited[0][0] = 1

    while queue:
        x, y, cnt = queue.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            nx = x + dx[i]          # 행
            ny = y + dy[i]          # 열
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    print(cnt)
    return 0


bfs()


'''
NOTE:

배추 문제랑 비슷한 것 같으면서도 최단 거리라는 조건이 하나 더 붙어서 뭔가 헷갈렸던 문제

처음에는 메모리 초과가 났는데, 32번라인에서 visited[nx][ny] == 0 조건을 추가했더니 해결됐다
방문 여부를 queue에 추가하기 전에 체크하지 않아서 그랬던 것 같다

또 처음 cnt 선언을 0으로 해서 헤매기도 했다...^^ 정말 어렵고도 어려운 알고리즘
2학기에 수업 꼭 듣고 만다
'''