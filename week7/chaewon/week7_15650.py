# BJ 15650 : N과 M (2) / SILVER III / 136ms

import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
ans = []


def back():
    if len(ans) == m:
        is_sorted = (sorted(ans) == ans)
        if is_sorted:                               # ans가 오름차순 정렬되어 있으면 print
            print(' '.join(map(str, ans)))
            return 0
    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()


back()


'''
NOTE:
15649번 문제와 거의 유사하다.
각 원소가 오름차순 정렬되어야 한다는 조건이 하나 추가된 것이다.

처음에는 for문 안에서, ans에 오름차순으로 원소를 append하려고 시도했었다.
그런데 너무 복잡해져서 다시 생각해봤는데,
print할 때 조건문을 걸어서 오름차순인 것들만 print하면 될 것 같았다.

리스트의 정렬 여부를 파악하는 법을 찾아봤고,
만약 ans가 오름차순 정렬되어 있으면 print하는 식으로 수정했다.
'''