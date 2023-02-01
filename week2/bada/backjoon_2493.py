'''
2493번 : 탑 (골드 5)

/* 여러 개 입력 받아 리스트로 만들기 */
list(map(int, input().split()))

#1

1. 입력 -> 리스트 저장
2. 출력 리스트 생성
3. 자신보다 인덱스가 더 작은 것 중에서 값이 더 큰 걸 발견하면 출력 리스트에 저장
4. 출력 리스트 print

3번에서 이중 for문 사용
O(n) = n^2

-> 시간 초과


# 2
stack 이용

1. 입력 -> 리스트 저장
2. 리스트 2개 선언 (최댓값 저장 스택, answer 저장)
3. 최댓값 스택에 자신보다 큰 값 있으면 answer에 그 값의 인덱스 저장 없으면 0 저장
4. answer 출력

'''


# 1
N = int(input())
top_list = list(map(int, input().split()))
# 2
max_stack = []
answer = []

#3
for i in range(N):
    while(max_stack):
        if(max_stack[-1][1] > top_list[i]):
            answer.append(max_stack[-1][0] + 1)
            break
        else:
            max_stack.pop()
    if not max_stack:
        answer.append(0)
    max_stack.append([i, top_list[i]])

#4
print(" ".join(map(str, answer)))


'''
/* 후기 */
아직 자료구조를 사용하는 습관 형성이 안 되어있다..
Stack을 써야하는지 생각도 못 했다

평소 사용하는 리스트, for문으로만 해결하려 하면 시간 초과를 맞닥뜨릴 수 밖에 없군
'''