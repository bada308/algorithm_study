'''
/*문제 정보 */
15486번 - 퇴사 2
난이도 - 골드 5

/*풀이 방법 */
계쏙 오류가 뜬다...
'''
import sys

n = int(input())
day = []
cost = []
dp = [0] *(n+1)

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    day.append(a)
    cost.append(b)

for i in range(1,n+1):
    if(i+day[i] <= n+1):
        dp[i+day[i]] = max(dp[i+day[i]], dp[i] + cost[i])
    dp[i+1] = max(dp[i+1],dp[i])

'''
/*오답 노트*/
/*느낀 점*/

'''