'''
/*문제 정보 */
1932번 - 정수 삼각형
난이도 - 실버 1

/*풀이 방법 */
이 문제에서 찾아낸 규칙은 삼각형 각 층마다 양쪽 맨끝의 숫자들은 더할 수 있는 경우의 수가 1개이고
안 쪽 숫자들은 왼쪽 오른쪽 대각선 중 더 큰값 더하면 된다.
이것을 맨 밑층까지 반복 후 맨 밑 줄의 최댓값을 호출하면 된다.
'''
n=int(input())
dp=[]
for i in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(dp[i])):
    if j==0:
      dp[i][j]=dp[i][j]+dp[i-1][j]
    elif j==len(dp[i])-1:
      dp[i][j]=dp[i][j]+dp[i-1][j-1]
    else:
      dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+dp[i][j]
print(max(dp[n-1]))
'''
/*오답 노트*/
/*느낀 점*/
다이나믹 프로그래밍 재밌으면서 코드 작성할 때 계속 헷갈린다... 퍼즐푸는거 같은 느낌
'''