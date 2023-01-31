'''
/*문제 정보 */
11053번 - 가장 긴 증가하는 부분 수열
난이도 - 실버 2

/*풀이 방법 */
dp에다가 처음 길이를 모두 1이라 저장 해놓고 for문으로 이용해 +1 더해서 dp 에서 최댓값 구하게 했다.
'''
n = int(input())
a = list(map(int,input().split()))
dp = [1]* n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''
/*오답 노트*/
/*느낀 점*/
이게 dp 인가 라는 생각이 든당
'''