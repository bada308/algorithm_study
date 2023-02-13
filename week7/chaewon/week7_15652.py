# BJ 15652 : N과 M (4) / SILVER III /

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().strip().split(' '))
ans = []

def back(x):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return 0

    for i in range(x, n + 1):
        ans.append(i)
        back(i)
        ans.pop()

back(1)


'''
NOTE:
처음엔 back()에 매개변수를 안줬는데 그러니까 시간초과가 떴다
15650번 문제 코드에 중복된 원소도 추가할 수 있게끔 코드를 짰었는데
재귀함수 호출하면서 for문 깊이가 깊어져서 시간 초과가 뜬 거였다.

매개 변수 설정을 해주면 재귀함수 호출할 때 i부터 체크하기 때문에
시간 초과가 뜨지도 않고, sorted로 비내림차순임을 체크할 필요도 없어진다.

어렵당
'''