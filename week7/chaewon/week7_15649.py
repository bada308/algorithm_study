# BJ 15649 : N과 M (1) / SILVER III / 168ms

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().strip().split(' '))

ans = []


def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return 0
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()


back()

'''
NOTE:
백트래킹과 depth-first search의 차이를 파악하기가 좀 어렵다

이 문제에서는 재귀함수를 이해하는 게 조금 힘들었다.
back()이 호출되면 그 안에서 for문이 다시 시행되는 형태인데 
이해가 잘 안돼서 시간이 좀 걸렸다

'''