'''
/* 문제 정보 */
15486번 - 퇴사 2
난이도 - 골드5

/* 풀이 방법 */
import sys

n = int(sys.stdin.readline().rstrip())
s = []
for _ in range(n):
    t, p = map(int, input().split())
    s.append(tuple((t, p)))

dp = [0 for _ in range(n)]
dp[0] = s[0][1]
for i in range(1, n):
    for j in range(i):
        if(i-j >= s[j][0] and i+s[i][0] <= n):
            dp[i] = max(dp[i], dp[j]+s[i][1])

print(max(dp))
-> 시간 초과,,, 암쏘 새드

'''


import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
    fin_date = i + t[i] - 1  # 당일 포함
    if fin_date <= n:  # 최종일 안에 일이 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])
print(max(dp))

# 지금까지 문제 중에 제일 이해가지 않는다... 나는 바보다
