'''
/*문제 정보 */
15650번 - N과 M(2)
난이도 - 실버 3
15649랑 다르게 방문기록이 필요 없을 것 같아 더 쉬울 것 같았는데 for문의 굴레에 빠져 이해가 안되느라
더 어려웠다. ....
/*풀이 방법 */
'''
def recur(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start,n+1):
        if i not in result:
            result.append(i)
            recur(i+1)
            result.pop()

n, m = map(int, input().split())
result  = []

recur(1)
'''
/*오답 노트*/
/*느낀 점*/
for 문 돌아갈 때 하나하나 천천히 머리속으로 시뮬레이션 돌리는게 어렵다..
'''