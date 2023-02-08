from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                continue
            if tmp[nx][ny] == 1:
                tmp[nx][ny] = tmp[x][y] + 1
                queue.append((nx, ny))
    for i in range(N):
        max_list.append(max(tmp[i])-1)

    return max(max_list)


def get_graph_sample():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'L':
                tmp[i][j] = 1
    return


N, M = map(int, input().split())
graph = []
tmp = []
max_list = []
result_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    graph.append(list(input()))

tmp = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            get_graph_sample()
            result_list.append(BFS(i, j))

print(max(result_list))