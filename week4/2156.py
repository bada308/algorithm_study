'''
/*문제 정보 */
2156번 - 포도주 시식
난이도 - 실버 1
/*풀이 방법 */
다른 문제와 마찬가지로 직접 경우의 수를 세봐서 했다.
dp[n]이 n개일 때 최대 양, a[n]이 n번째 양
'''
n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
dp = [0]
dp.append(a[1])
if n > 1:
    dp.append(a[1] + a[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + a[i - 1] + a[i], dp[i - 2] + a[i]))
print(dp[n])
'''
/*오답 노트*/
/*느낀 점*/
검색하면서 사람들이 dp로 이름 자주 하길래 뭐지 해서 검색 해봤는데 dynamic programming
이번 주차 주제 동적 게획법이었다.. 바보다 바보
'''