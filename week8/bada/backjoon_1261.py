'''
/* 문제 정보 */
1261번 - 알고스팟
난이도 - 골드4

/* 풀이 방법 */
비용이 0 or 1이면 0-1 BFS를 이용!

'''
import sys
from collections import deque

w, h = map(int, sys.stdin.readline().rstrip().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(h)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 0
queue = deque()
queue.append((0, 0, 0)) # (x, y, damage)
graph[0][0] = -1

while queue:
    x, y, damage = queue.popleft();

    if (x == h-1) and (y == w-1):
        answer = damage
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 0:
                queue.appendleft((nx, ny, damage))
                graph[nx][ny] = -1
            
            if graph[nx][ny] == 1:
                queue.append((nx, ny, damage + 1))
                graph[nx][ny] = -1
            
print(answer)



'''
/* 오답노트 */

/* 느낀점 */

'''