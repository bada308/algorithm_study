'''
/*문제 정보 */
11726번 - 2Xn 타일링
난이도 - 실버 3

/*풀이 방법 */
n=2,3,4,5 일 떼 까지 구해 점화식이 n = (n-1)+ (n-2)인 것을 구했당.
'''
dp = [0,1,2]

for i in range(3,1001):
    dp.append(dp[i-1]+dp[i-2])

n = int(input())

print(dp[n] % 10007)
'''
/*오답 노트*/
/*느낀 점*/
저번 문제보다 쉬웠다!
'''