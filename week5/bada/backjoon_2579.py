'''
/* 문제 정보 */
2579번 - 계단 오르기
난이도 - 실버3

/* 풀이 방법 */


'''
import sys

n = int(sys.stdin.readline().rstrip())
stair = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]

if len(stair)<=2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[-1])
# 런타임 에러 떠..?
# 계단 개수가 1개 or 2개일 때는 예외로 빼줘야 런타임 에러가 안 생긴댜~~