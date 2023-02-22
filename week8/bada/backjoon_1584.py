'''
/* 문제 정보 */
1584번 - 게입
난이도 - 골드5

/* 풀이 방법 */


'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[0] * 501 for _ in range(501)]

n = int(input()) # 위험 구역 수
danger = [list(map(int, input().split())) for _ in range(n)]
m = int(input()) # 죽음 구역 수
death = [list(map(int, input().split())) for _ in range(m)]

for i in range(501):
    for j in range(501):
        for x1, y1, x2, y2 in danger:
            if (min(x1, x2) <= i <= max(x1, x2)) and (min(y1, y2) <= j <= max(y1, y2)):
                graph[i][j] = 1
        for x1, y1, x2, y2 in death:
            if (min(x1, x2) <= i <= max(x1, x2)) and (min(y1, y2) <= j <= max(y1, y2)):
                graph[i][j] = 2

answer = 0
queue = deque()
queue.append((0, 0, 0)) # (x, y, damage)
graph[0][0] = 2
can_reach = False

while queue:
    x, y, damage = queue.popleft()

    if (x == 500) and (y == 500):     # (500, 500)에 도착하면 종료
        can_reach = True
        answer = damage
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx <= 500) and (0 <= ny <= 500) and (graph[nx][ny] != 2):
            if graph[nx][ny] == 0:
                queue.appendleft((nx, ny, damage))
                graph[nx][ny] = 2

            if graph[nx][ny] == 1:
                queue.append((nx, ny, damage + 1))
                graph[nx][ny] = 2

if can_reach:
    print(answer)
else:
    print(-1)


'''
/* 오답노트 */

/* 느낀점 */

'''