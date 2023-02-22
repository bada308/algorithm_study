import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return


N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]
distance = [INF for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

Dijkstra(Y)
distance = [i * 2 for i in distance]


distance[Y] = INF
result = 0
left_step = X
heapq.heapify(distance)

while distance:
    dist = heapq.heappop(distance)
    if left_step >= dist:
        left_step -= dist
    else:
        left_step = X
        left_step -= dist
        result += 1

        if dist == INF:
            print(result)
            break
        if dist > X:
            print(-1)
            break

"""
44번째줄에 >=가 아니라 > 했다가 찾느라 엄청 시간이 오래 걸렸다........ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
"""
