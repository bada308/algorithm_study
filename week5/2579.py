'''
/*문제 정보 */
2579번 - 계단 오르기
난이도 - 실버 3

/*풀이 방법 */
예전에 풀었던 것처럼 이전에 밟은 계단의 경우의 수 중에 최댓값을 고르는 식으로 풀었당
'''
import sys
n = int(sys.stdin.readline())
a = [0]*301
dp = [0]*301

for i in range(n):
    a[i] = int(sys.stdin.readline())

dp = [0]*n
dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(a[1]+a[2], a[0] + a[2])

for i in range(3,n):
    dp[i] = max(dp[i - 3] + a[i - 1] + a[i], dp[i - 2] + a[i])

print(dp[n-1])


'''
/*오답 노트*/
/*느낀 점*/
런타임 에러 뜨길래 3번이나 고쳐봤는데 계속 에러...
'''