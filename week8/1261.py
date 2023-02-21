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
            if nx < 0 or ny < 0 or nx >= M or ny >= N or visited[nx][ny]:
                continue
            distance[nx][ny] = min(distance[nx][ny], distance[x][y] + graph[nx][ny])
            heapq.heappush(q, (distance[nx][ny], (nx, ny)))
            visited[nx][ny] = True
            print(nx, ny)
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


"""
처음에 23번째줄에서 q에 distance[nx][ny]를 push 해주지 않고 graph[nx][ny]를 push 해줘서 안됐었다.
두번째는 24번째줄에서 for 문이 끝난 후 x,y 번째를 visit 처리해서 틀렸었다. #visited[x][y] = True
↑ 이 위에부분을 다른 사람들 코드를 보고 고쳤었는데 왜 고쳐야하는지 모르고 visited[x][y] = True가 맞는 줄 알았다.
근데 내가 20번째줄에서 visited[x][y]가 아닌 visited[nx][ny]를 조건으로 달았기 때문에 visited[nx][ny] = True 로 써주어야 된다.
근데 이 코드가 왜 맞는지 도대체 모르겠다.

드디어 알았다.
본래 다익스트라 문제들은 한곳에서 다른 곳으로 갈 때(A->B) 바로 가는 것과 거쳐 가는것(A->C->B)이 있어 이 둘 중 뭐가 더 빠른지 비교를 해야하지만
이 문제는 그냥 갈 수 있는 모든 길을 최솟값으로 가기 때문에 간 곳 바로 다음 길이 그 길의 최솟값이다.
따라서 visited[x][y]를 push 하는게 아니라 visited[nx][ny]를 push 해도 상관없다.
오히려 visited[nx][ny]를 push 하는게 효과적이다. visited[x][y]를 push 하면 할 필요 없는 계산을 하게 된다.

"""

"""
#원래 작성하고 싶었던 코드
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
result = 0
print(Dijkstra())
"""

"""
근데 내가 원래 작성하려던 코드가 더 시간이 많이 걸리는지 모르겠다. 왜지...?
첫 번째 64ms
두 번째 124ms
"""