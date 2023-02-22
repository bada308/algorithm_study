'''
/* 문제 정보 */
20007번 - 떡 돌리기
난이도 - 골드4

/* 풀이 방법 */


'''
import sys
import heapq

INF = int(1e9)

n, m, x, y = map(int, sys.stdin.readline().split()) # 이웃집 수, 도로 수, 하루 최대 거리, 성현이집

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

def dijkstra():
    distance = [INF] * (n)
    distance[y] = 0 # 시작노드 -> 시작노드 거리 기록
    pq = []
    heapq.heappush(pq, [0, y]) # 시작노드 정보 heapq에 삽입

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

distances = dijkstra()
distances_idx = [[distance, idx] for idx, distance in enumerate(distances)]
distances_idx.sort()

if distances_idx[-1][0] * 2 > x: print(-1)
else:
    day = 1
    cur = 0
    for distance, idx in distances_idx:
        if cur + 2 * distance <= x:
            cur += 2 * distance
        else:
            day += 1
            cur = 2 * distance
    print(day)

'''
/* 오답노트 */

/* 느낀점 */

'''