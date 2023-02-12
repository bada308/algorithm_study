'''
/*문제 정보 */
15649번 - N과 M(1)
난이도 - 실버 3

/*풀이 방법 */
n,m을 받은 후 결과값과 방문 기록 리스트를 만들어 준 다음 dfs 느낌으로 했다.
결과리스트의 len 값이 m과 같을 때 출력하게 해준 뒤 for문으로 방문 기록을 확인하며 for가 돌아가게 했다.
'''


def recur():
    if len(result) == m:
        print(' '.join(map(str, result)))

    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur()
            result.pop()
            visited[i] = False

n, m = map(int, input().split())
result  = []
visited = [False] * (n + 1)

recur()


'''
/*오답 노트*/
/*느낀 점*/
dfs 보다 쉬운 느낌?을 받았다. 문제가 쉬워서 그런가.. 
'''