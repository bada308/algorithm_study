'''
/* 문제 정보 */
15652번 - N과 M (4)
난이도 - 실버 3

/* 풀이 방법 */


'''
import sys

n, m = map(int, input().split())
s = []

def getSequence():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
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