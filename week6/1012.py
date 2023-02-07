'''
/*문제 정보 */
1012번 - 유기농 배추
난이도 - 실버 2

/*풀이 방법 */
그래프로 작성 후 (0,0)부터 차례로 1인 곳을 찾는다. 1인 곳에서 상하좌우로 계속 1을 찾고 0으로 바꿔준다.
1을 처음 찾았을 때만 카운트를 세면 지렁이 수를 찾을 수 있다.
'''
import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x <= -1 or x >= N or y<= -1 or y>= M:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True
  return False

answer = []
for _ in range(T):
  M, N, K = list(map(int, sys.stdin.readline().split()))

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt +=1

  print(cnt)
'''
/*오답 노트*/
/*느낀 점*/
재귀 한도 깊이 설정하는 sys.setrecursionlimit 코드도 새로 배웠다..
'''