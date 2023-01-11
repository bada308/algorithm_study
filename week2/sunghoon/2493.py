'''
/*문제 정보 */
2493번 - 탑
난이도 - 골드 5

/*풀이 방법 */
1.수신하는 탑이 없으면 0을 출력해야 하므로 answer 모두 0으로 시작
2.num의 숫자를 하나씩 호출해 스택에 넣고 그 다음 숫자를 호출했을 때 스택에 있는 숫자가 더 큰지 비교
3.더 작으면 해당 숫자를 스택에서 꺼내고, 더 크면 그 값의 인덱스값 +1 저장
4.최종 출력시 리스트 형태가 아닌 숫자가 나열되는 형태로 출력해야 하니 *answer
'''
n = int(input())
num = list(map(int,input().split()))

stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if num[stack[-1]-1] >= num[i]:
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(i+1)
print(*answer)
'''
/*오답 노트*/
/*느낀 점*/
이론 공부 후, 바로 코드 작성을 하다보니 쉽지 않았다... 
이론은 쉬웠으나 문제로 들어가니 어려워...
스택 연산자랑 후위 표기식에 대한 공부가 더 필요할 것 같다.
'''