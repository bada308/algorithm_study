from _collections import deque


def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


count_node, count_edge, v = map(int, input().split())
graph = [[] for i in range(count_node + 1)]
visited = [False] * (count_node + 1)

for i in range(count_edge):
    node_1, node_2 = map(int, input().split())
    graph[node_1].insert(i, node_2)
    graph[node_2].insert(i, node_1)

for i in range(len(graph)):
    graph[i].sort()

DFS(graph, v, visited)
print()
visited = [False] * (count_node + 1)
BFS(graph, v, visited)

# 그냥 배운것과 똑같은 함수를 쓰면 됐어서 잘 풀렸다.