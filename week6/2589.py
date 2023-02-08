from collections import deque


def BFS(x, y, visited):
    queue = deque()
    if not visited[x][y]:
        queue.append((x, y))
        visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                continue
            if tmp[nx][ny] == 1 and not visited[nx][ny]:
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
                visited[i][j] = False
    return


N, M = map(int, input().split())
graph = []
tmp = []
max_list = []
result_list = []
visited = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    graph.append(list(input()))

tmp = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            get_graph_sample()
            result_list.append(BFS(i, j, visited))

print(max(result_list))

"""
설마 BFS를 전부 돌려야하나 해서 해봤는데 맞았다..
그런데 각 L마다 tmp를 초기화시킬거였으면 시간이 왕창 더 걸리더라도 DFS를 썼어도 됐을 듯
"""