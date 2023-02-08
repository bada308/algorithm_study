# BJ 2589 / GOLD V / 752ms

import sys
from collections import deque

sys.setrecursionlimit(10000)

n, m = map(int, input().split(' '))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    cnt = 0
    queue.append((x, y))
    visited[x][y] = 1           # 놓친 부분

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])                         # 현재 위치에서 가장 먼 육지까지의 거리+1 값을 구함
                queue.append((nx, ny))
    return cnt - 1


result = 0

for i in range(n):
    for j in range(m):
        if i > 0 and i + 1 < n:
            if graph[i - 1][j] == "L" and graph[i + 1][j] == "L":
                continue
        if j > 0 and j + 1 < m:
            if graph[i][j - 1] == "L" and graph[i][j + 1] == "L":
                continue

        if graph[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            result = max(result, bfs(i, j))

print(result)


'''
NOTE:
대부분의 로직은 구현했는데, cnt 구하는 과정에서 막혔다ㅠ

32번 라인 : visited[nx][ny] = visited[x][y] + 1 를 통해, 현재 위치에서 각 육지위치까지의 거리를 구할 수 있게 된다는 것,
51번 라인 : 육지좌표 간 가장 거리가 먼 값을 구하는 과정인데, 여기서는 바로바로 result와 bfs()를 비교하는 데 max()를 써도 되지만
           list를 만들고 bfs()값을 append한 뒤 max(list)해도 된다. 

42~47번 라인 : 백트래킹 코드. 육지이지만 가장자리가 아닌 부분을 제외하는 과정이다.
              육지이지만 가장자리가 아닌 부분을 지나면, 가장 먼 최단거리에 해당할 수 없기 때문에 애초부터 배제해주는 것
              이 코드가 없으면 pypy3로 제출해야 시간초과가 안난다
              이 부분이 있어야 python3로 제출 가능하다

골드 v라 그런가 확실히 어렵다!!! 그래도 점점 나아지는 중이당
'''