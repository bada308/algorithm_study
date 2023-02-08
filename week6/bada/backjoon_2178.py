'''
/* 문제 정보 */
2178번 - 미로 탐색
난이도 - 실버1

/* 풀이 방법 */


'''
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


queue = deque([(0, 0)])
visited[0][0] = 1

def bfs():
    while queue:
        x, y = queue.popleft()

        if (x == n-1) and (y == m-1):
            print(visited[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if (visited[nx][ny] == 0) and (maze[nx][ny] == 1):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny)) 


bfs()






'''
/* 오답노트 */

/* 느낀점 */


'''