import sys
sys.setrecursionlimit(10**6)


def DFS(x, y, visited, color):
    if x <= -1 or x >= a or y <= -1 or y >= a:
        return False

    if not visited[x][y] and graph[x][y] == color:
        visited[x][y] = True
        DFS(x + 1, y, visited, color)
        DFS(x - 1, y, visited, color)
        DFS(x, y + 1, visited, color)
        DFS(x, y - 1, visited, color)
        return True
    return False


def set_color():
    for i in range(a):
        for j in range(a):
            if graph[i][j] == 'R' or graph[i][j] == 'G':
                graph[i][j] = 'Y'


a = int(input())
visited = [[False for _ in range(a)] for _ in range(a)]
graph = []
for i in range(a):
    graph.append(list(input()))

result = 0
for i in range(a):
    for j in range(a):
        if DFS(i, j, visited, graph[i][j]):
            result += 1

print(result, end=" ")
set_color()
result = 0
visited = [[False for _ in range(a)] for _ in range(a)]
for i in range(a):
    for j in range(a):
        if DFS(i, j, visited, graph[i][j]):
            result += 1

print(result)

"""
배추 문제랑 똑같아서 잘 풀렸다.
근데 재귀 깊이 설정을 또 안해줬어서 오류가 떴었다.
DFS랑 재귀 깊이 설정은 짝궁으로 생각해야될 듯... 
"""