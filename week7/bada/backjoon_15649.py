'''
/* 문제 정보 */
15649번 - N과 M (1)
난이도 - 실버 3

/* 풀이 방법 */
숫자를 선택하는 경우의 수로 이루어진 트리
백트래킹은 기본적으로는 모든 경우의 수를 탐색한다는 브루트 포스 전략을 취하지만,
처리 속도 향상을 위한 가자치기가 중요한 역할을 함

'''
import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:  # 가지치기?
      continue
    s.append(i)
    f()
    s.pop()

f()
'''
/* 오답노트 */

/* 느낀점 */

'''