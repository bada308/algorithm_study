import sys
sys.setrecursionlimit(10**6)


def get_graph():
    M, N, cabbage = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(cabbage):
        y, x = map(int, input().split())
        graph[x][y] = 1
    return graph


def DFS(graph, x, y):
    if x >= len(graph) or x <= -1 or y >= len(graph[0]) or y <= -1:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0

        DFS(graph, x, y + 1)
        DFS(graph, x, y - 1)
        DFS(graph, x - 1, y)
        DFS(graph, x + 1, y)
        return True
    return False


Test_case = int(input())
for i in range(Test_case):
    graph = get_graph()
    row = len(graph)
    column = len(graph[0])

    result = 0

    for j in range(row):
        for k in range(column):
            if DFS(graph, j, k) == 1:
                result += 1
    print(result)

"""
처음에 런타임 오류가 떴었는데 백준의 채점서버에서의 최대 재귀깊이가 1000이여서 오류가 떴다.

import sys
sys.setrecursionlimit(10**6)

재귀 깊이를 변경해주니 맞았다.

재귀를 사용하지 않는 BFS로도 풀어봐야겠다.
"""
