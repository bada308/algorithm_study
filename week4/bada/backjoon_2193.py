'''
/* 문제 정보 */
2193번 - 이친수
난이도 - 실버3

/* 풀이 방법 */


'''
s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])
    