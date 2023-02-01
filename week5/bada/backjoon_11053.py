'''
/* 문제 정보 */
11053번 - 가장 긴 증가하는 부분 수열
난이도 - 실버2

/* 풀이 방법 */
어려우어어ㅓㅇ

import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, input().split()))

count = 1
for i in range(1, N):
    if A[i] > A[i-1]:
        count += 1
    else:
        A[i] = A[i-1]

print(count)
-> 처음 풀이,, DP 사용 안 하구 틀렸습니다 뜸
'''
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))