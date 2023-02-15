'''
/* 문제 정보 */
15650번 - N과 M (2)
난이도 - 실버 3

/* 풀이 방법 */


'''
import sys

n, m = map(int, sys.stdin.readline().split())
s = []

def getSequence():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:
            continue
        if len(s) > 0 and i < s[-1]:
            continue
        s.append(i)
        getSequence()
        s.pop()

getSequence()

'''
/* 오답노트 */

/* 느낀점 */

'''