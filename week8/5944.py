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
    for i in range(1, P + 1):
        if distance[i] == INF:
            distance[i] = -1
    return


C, P, PB, PA1, PA2 = map(int, input().split())
graph = [[] for _ in range(P + 1)]
distance = [INF for _ in range(P + 1)]
for i in range(C):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

Dijkstra(PB)
start_to_PA1 = distance[PA1]
start_to_PA2 = distance[PA2]
distance = [INF for _ in range(P + 1)]
Dijkstra(PA1)
PA1_to_PA2 = distance[PA2]

print(min(start_to_PA1 + PA1_to_PA2, start_to_PA2 + PA1_to_PA2,
          start_to_PA1 * 2 + start_to_PA2, start_to_PA2 * 2 + start_to_PA1))

"""
최솟값이 나올 수 있는 경우의 수가 4가지 있다.
1. start -> PA1 -> PA2
2. start -> PA2 -> PA1
3. start -> PA1 -> start -> PA2
4. start -> PA2 -> start -> PA1

따라서 start -> PA1값과 start -> PA2값과 PA1 -> PA2값을 구했다.
"""