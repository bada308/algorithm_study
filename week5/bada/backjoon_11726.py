'''
/* 문제 정보 */
11726번 - 2*n 타일링
난이도 - 실버3

/* 풀이 방법 */
백준 9095번 1, 2, 3 더하기와 유사
1X2, 2X2 타일로 2XN 채우기 = 1과 2를 더해서 n 만들기
'''
import sys

n = int(sys.stdin.readline().rstrip())
 
dp = [0, 1, 2] # 초기값

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
   
print(dp[n]%10007)