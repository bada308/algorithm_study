# BJ 10026 / GOLD V / 96ms

import sys
from collections import deque

sys.setrecursionlimit(10000)            # 런타임 에러 방지 : 기본 재귀 깊이 제한 = 1000으로 매우 얕음, 10000으로 변경함으로써 런타임 오류 해결, 재귀함수 사용할 때는 꼭 적어두는 게 좋음

n = int(input())

graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

normal_cnt = 0
rb_cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph[i] = list(sys.stdin.readline().strip())


def dfs(x, y):
    visited[x][y] = 1
    current_color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0 and current_color == graph[nx][ny]:
                dfs(nx, ny)
    return 0


# 정상인이 볼 때
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            normal_cnt += 1


# 적록색약인 사람이 볼 때 -> graph에서 G를 R로 바꾸어 줌
for row in range(n):
    for column in range(n):
        if graph[row][column] == 'G':
            graph[row][column] = 'R'

# visited 초기화
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            rb_cnt += 1

print(normal_cnt, rb_cnt)


'''
NOTE:
계속 비슷한 문제인 것 같은데 조금만 달라져도 풀기 어려운 주제인 것 같다 흑

'''