'''
17298번 : 오큰수 (골드 4)

알고리즘 분류 : 자료구조 스택

1. 입력
2. 스택 & 정답 리스트 생성
3. 스택을 이용해 오큰수 구하기
4. 정답 출력
'''

# 1
N = int(input())
input_list = list(map(int, input().split()))

# 2
stack = []
answer = [-1 for i in range(N)]

# 3
for i in range(N-1, -1, -1):
    while(stack):
        if(stack[-1] > input_list[i]):
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(input_list[i])

# 4
print(' '.join(map(str, answer)))


'''
/* 후기 */
탑 문제랑 유사함
알고리즘 분류가 스택인 걸 알면 풀 수 있는데 몰랐을 때는 풀이가 떠오르지 않았다.
'''