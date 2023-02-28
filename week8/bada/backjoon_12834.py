'''
/* 문제 정보 */
12834번 - 주간 미팅
난이도 - 골드4

/* 풀이 방법 */


'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, v, e = map(int, input().split())
k, cr = map(int, input().split())
homes = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]
visited = [False] * (v+1)


for _ in range(e):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])


# 다익스크라 알고리즘
def dijkstra(start):
    distance = [INF] * (v+1)
    distance[start] = 0 # 시작노드 -> 시작노드 거리 기록
    pq = []
    heapq.heappush(pq, [0, start]) # 시작노드 정보 heapq에 삽입

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        # heapq에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 무시
        if distance[cur_node] < cur_cost : continue

        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next_node, next_cost in graph[cur_node]:
            if distance[next_node] > next_cost + cur_cost:
                distance[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])
    return distance

distance_k = dijkstra(k)
distance_cr = dijkstra(cr)
total = 0

for home in homes:
    dist_k = distance_k[home]
    dist_cr = distance_cr[home]
    
    if dist_k == INF: total -= 1
    else: total += dist_k

    if dist_cr == INF: total -= 1
    else: total += dist_cr

print(total)

'''
/* 오답노트 */

/* 느낀점 */

'''