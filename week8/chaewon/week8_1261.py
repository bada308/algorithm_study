# BJ 1261 : 알고스팟 / GOLD IV / 80ms

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split(' '))

miro = []
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    miro.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                if miro[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))

print(visited[n-1][m-1] - 1)
