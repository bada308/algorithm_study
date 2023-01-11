'''
/*문제 정보 */
17298번 - 오큰수
난이도 - 골드 4

/*풀이 방법 */
1.오큰수가 없을시 -1 출력해야하므로 answer 모두 -1로 시작
2.입력된 숫자의 인덱스를 스택에 저장
3.인덱스의 숫자가 스택 맨 위 인덱스번째 숫자보다 크면 스택 맨위 인덱스번째 숫자의 오큰수로 i번째 숫자 저장
4.오큰수를 찾았으면 해당 인덱스는 스택에서 제거하고, 스택의 다음 인덱스가 i번째 숫자보다 작은지 다시 확인
'''
n = int(input())
num = list(map(int,input().split()))

stack = []
answer = [-1 for _ in range(n)]

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        answer[stack.pop()] = num[i]
    stack.append(i)
print(*answer)
'''
/*오답 노트*/
/*느낀 점*/
스택을 사용하지 않았을 때 시간초과가 나왔다. 왜 자료구조 공부를 해야 하는지 느낌..
코드 작성하는데는 2493번을 풀어서 그 문제 코드랑 다를게 별로 없었다. 
'''