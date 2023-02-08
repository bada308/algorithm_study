'''
/* 문제 정보 */
1012번 - 유기농 배추
난이도 - 실버2

/* 풀이 방법 */


'''

import sys 
sys.setrecursionlimit(10000) # 파이썬에서 재귀로 문제 풀 때 필수

t = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if field[nx][ny] == 1:
                field[nx][ny] = 0
                dfs(nx, ny)


for _ in range(t):
    m, n, k = map(int, input().split()) # 열, 행, 개수
    field = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    # 배추 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                dfs(a, b)
                cnt += 1
    print(cnt)



    

    



'''
/* 오답노트 */
dfs랑 bfs 모두 사용할 수 있는데 bfs는 생각하기가 너무 어렵다..1!!!!

/* 느낀점 */


'''