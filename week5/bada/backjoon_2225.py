'''
/* 문제 정보 */
2225번 - 합분해
난이도 - 골드5

/* 풀이 방법 */
https://jyeonnyang2.tistory.com/54
이해가 쏙쏙 선생님인가

'''
n, k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)

# DP에서 느껴지는 알고리즘의 벽,,, 아임쿠라잉