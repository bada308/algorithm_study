'''
/*문제 정보 */
2225번 - 합분해
난이도 - 골드 5

/*풀이 방법 */
n,k이 1일 때부터 하나하나 세가면서 점화식을 구했다..
'''
n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


print(dp[k][n] % 1000000000)

'''
/*오답 노트*/
/*느낀 점*/
매우 힘들다.
'''