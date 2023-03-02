# BJ 14889 : 스타트와 링크 / SILVER II /

import sys

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = int(1e9)


def dfs(depth, idx):
    global min_diff
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1 - power2))
        return 0

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0


dfs(0, 0)
print(min_diff)


'''
NOTE:
(1~n)번까지의 팀원을 두 팀으로 나누어, 팀별로 팀원 간의 모든 능력치를 더해 빼는 방향

그래서 처음에 스타트 팀/링크 팀을 구분했는데,
스타트 팀을 기준으로 잡고 (1~n)번에서 n / 2 개를 랜덤 추출하고,
나머지 수를 링크 팀으로 넣어주었다
그 후 두 팀간의 능력치합 차이를 구하는 것을 진행했었다.

여기서 문제는, 두 개의 팀으로 나눌 때 스타트 팀을 랜덤 추출하는 것이 아니라,
팀이 나뉠 수 있는 모든 경우의 수를 고려해야 하는 것이었다.

그래서 15650번을 참고해서, n에서 n/2 개의, 중복되지 않는 배열을 함수를 사용해서 뽑아내려고 했는데
그 부분이 막혀서 결국 찾아봤다ㅠ
'''