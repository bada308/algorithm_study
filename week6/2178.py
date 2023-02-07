'''
/*문제 정보 */
2178번 - 미로 탐색
난이도 - 실버 1

/*풀이 방법 */
(0,0)에서 출발해 (n-1,m-1)까지 bfs로 가면서 한칸 이동할 때 마다 1을 더해준다.
그러면 그래프(n-1,m-1)의 값이 최단거리 값이다.

'''
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue


            if graph[nx][ny] == 0:
                continue


            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    return graph[N - 1][M - 1]


print(bfs(0, 0))
'''
/*오답 노트*/
/*느낀 점*/
bfs는 너무 어렵다. 진짜 어렵다. 못하겠다.
'''