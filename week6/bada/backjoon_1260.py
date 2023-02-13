'''
/* 문제 정보 */
1260번 - DFS와 BFS
난이도 - 실버2

/* 풀이 방법 */


'''

from collections import deque

n, m, v = map(int, input().split())
edge = [[] for _ in range(n+1)]

for i in range(m):
    p1, p2 = map(int, input().split())
    edge[p1].append(p2)
    edge[p2].append(p1)

for e in edge:
    e.sort()

BFS_check = [False for _ in range(n+1)]
DFS_check = [False for _ in range(n+1)]

def dfs(x):
    DFS_check[x] = True
    print(x, end=' ')
    for y in edge[x]:
        if DFS_check[y] == False:
            dfs(y)

def bfs():
    queue = deque([v])
    BFS_check[v] = True
    while queue:
        left = queue.popleft()
        print(left, end=' ')
        for i in edge[left]:
            if not BFS_check[i]:
                BFS_check[i] = True
                queue.append(i)

dfs(v)
print()
bfs()
print()




'''
/* 오답노트 */
dfs는 생각해내기 쉬웠는데 bfs가 어려웠당 양방향 큐를 이용하는군
/* 느낀점 */
개념을 아는 것과 코드로 짜는 건 또 다른 어려움이다

'''