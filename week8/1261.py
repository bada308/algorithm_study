'''
/*문제 정보 */
1261번 - 알고스팟
난이도 - 골드 4
/*풀이 방법 */
graph에 맵을 받아주고, dist에 벽을 깬 횟수를 저장해준다.
bfs로 맵으 범위 안에서 0인지 1인지 구분해 깬 횟수를 저장해 출력해준다.
'''
from collections import deque
N, M = map(int, input().split())
graph = []

for i in range(M):
    graph.append(list(map(int, input())))

dist = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    dist[0][0] = 0  # 첫번째 벽을 깬 횟수는 0으로 초기화

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if dist[nx][ny] == -1:

                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft([nx, ny])


                else:
                    dist[nx][ny] = dist[x][y] + 1  # 전의 벽을 깬 횟수에서 +1 해준다.
                    queue.append([nx, ny])  # 큐의 맨 오른쪽에 추가

bfs(0, 0)
print(dist[M - 1][N - 1])

'''
/*오답 노트*/
/*느낀 점*/
그냥 너무 어렵다. 어려워... 이해가 쉽지 않다.
'''