'''
/*문제 정보 */
15652번 - N과 M(4)
난이도 - 실버 3

/*풀이 방법 */
15650 풀이에서 if 조건을 없애주고 recur(i)로 바꿔주면 해결
'''
def recur(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start,n+1):
            result.append(i)
            recur(i)
            result.pop()

n, m = map(int, input().split())
result  = []

recur(1)
'''
/*오답 노트*/
/*느낀 점*/

'''