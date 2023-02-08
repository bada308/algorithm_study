'''
/* 문제 정보 */
10026번 - 적록색약
난이도 - 골드5

/* 풀이 방법 */


'''
import sys
sys.setrecursionlimit(1000000)

n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    

def dfs(x, y):
    visited[x][y] = 1
    current_color = matrix[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0:
                if matrix[nx][ny] == current_color:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            three_cnt += 1



for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)




'''
/* 오답노트 */
재귀 함수 제한 푸는 거 추가 안 하면 런타임에러 뜸

/* 느낀점 */


'''