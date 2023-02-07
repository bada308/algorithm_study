'''
/*문제 정보 */
1260번 - DFS와 BFS
난이도 - 실버 2

/*풀이 방법 */
deque 모듈을 이용했고 각 리스트들을 초기화하고 방문 리스트는 false값으로
초기화해 방문한 값은 true로 바꿨다.

'''
import sys
from collections import deque

def dfs(V):
    dfs_visited[V] = True
    print(V, end =' ')
    for i in range(1, N+1):
        if not dfs_visited[i] and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    bfs_visited[V] = True
    queue = deque()
    queue.append(V)
    while queue:
        popV = queue.popleft()
        print(popV, end=' ')
        for i in range(1, N+1):
            if not bfs_visited[i] and graph[popV][i] ==1:
                queue.append(i)
                bfs_visited[i] = True

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[0]* (N+1)for _ in range(N+1)]
dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(V)
print()
bfs(V)
'''
/*오답 노트*/
/*느낀 점*/
이 기본 문제를 풀기 위해 dfs,bfs 개념 본 시간만 엄청 많은 것 같다.
deque 모듈 사용법도 알게 되고 많이 배운 것 같지만 아직 너무너무 어렵다.
dfs보다 bfs가 더 어려운 것 같다...
https://kbwplace.tistory.com/114
'''