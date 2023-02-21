import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def Dijkstra():
    q = []
    heapq.heappush(q, (0, (0, 0)))
    distance[0][0] = 0
    while q:
        dist, now = heapq.heappop(q)
        x = now[0]
        y = now[1]
        if x == M - 1 and y == N - 1:
            return distance[-1][-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N or visited[x][y]:
                continue
            distance[nx][ny] = min(distance[nx][ny], distance[x][y] + graph[nx][ny])
            heapq.heappush(q, (distance[nx][ny], (nx, ny)))

        visited[x][y] = True
    return distance[-1][-1]


N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input().rstrip())))
visited = [[False for _ in range(N)] for _ in range(M)]
distance = [[INF for _ in range(N)] for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(Dijkstra())