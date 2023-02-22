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
    for i in range(1, V + 1):
        if distance[i] == INF:
            distance[i] = -1
#    distance[start] = 0
    return


# 팀원, 장소, 도로 수
N, V, E = map(int, input().split())
# KIST, 씨알푸드
A, B = map(int, input().split())
# 팀원 집 주소
team_member = list(map(int, input().split()))
graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

for i in range(1, E + 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

result = 0
for member in team_member:
    Dijkstra(member)
    result += distance[A] + distance[B]
    distance = [INF for _ in range(V + 1)]

print(result)

"""
1번째 노드에서 2번째,3번째 노드로 가는 길이 있다고 할 때 2로 가는게 1의 비용이 들고 3으로 가는게 5라고 할 때,
start 에 1을 넣어주고 비용을 0으로 잡는 코드를 썼다고 생각했는데 22번째 코드가 없을 때는
2로 갔다가 다시 1로 와서 2로 가는 비용 * 2가 비용으로 잡혀버린다... 22번째 코드는 땜빵용 코든거 같은데 나중에 제대로 고쳐봐야겠다..

역시 반례나 오류 찾을 때는 생각하는것보다
print 써서 확인하거나 디버그해보는게 최고라는 걸 다시 느꼈다...

생각해보니깐 문제랑 상관 없는 오륜거 같은데 왜 틀렸다고 나오지...?
그리고 22번째가 아니라 코드가 시작할 때 0으로 초기화하면 다시 돌아갈 일이 없구나! 10번째줄에 추가함
"""