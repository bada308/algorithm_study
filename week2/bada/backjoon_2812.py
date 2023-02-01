'''
2812번 : 크게 만들기 (골3)
알고리즘 유형 : 자료구조, 그리디, 스택

1. 입력
2. 스택 생성
3. 가장 큰 수 구하기
3.1. 스택에 자기 보다 작은 값이 맨 뒤에 있으면 pop하고(반복), 자기 자신 append
3.2. pop 한 횟수가 K가 넘으면 pop 중지
3.3 최종 stack에 담긴 수가 정담
4. 정답 출력
'''

# 1
N, k = input().split()
N = int(N)
k = int(k)
num = input()
input_list = list(map(int, str(num)))

#2 
stack = []

# 3
cnt = 0

for i in range(N):
    while(stack and cnt < k):
        if(stack[-1] < input_list[i]):
            stack.pop()
            cnt += 1
        else:
            break
    stack.append(input_list[i])

# 4
print(''.join(map(str, stack[:N-k]))) # Check


'''
/* 오답노트 */
# 4
stack에서 index 0부터 N-k-1까지만 출력!
[:N-k] 안 넣으면 빈 리스트 값까지 출력된다 


/* 후기 */
이 문제도 알고리즘 분류에서 힌트 얻고 해답 생각해냈다!
'''