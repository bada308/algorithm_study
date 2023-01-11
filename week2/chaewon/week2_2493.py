import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))


stack = []                                                      # 빈 스택 생성
result = [0 for i in range(n)]                                  # 탑의 개수만큼 0으로 채워진 리스트

'''
** enumerate() 함수 ; 세다(count)의 의미
python에서 리스트와 같은 자료형의 인덱스와 원소에 함께 접근할 때 용이

보통 아래처럼 len()으로 자료형의 전체 길이를 사용해서 루프문 돌림
for idx in range(len(towers)):
    print(idx, towers[idx])
    
but enumerate() 사용하면 tuple 값을 출력함 (인덱스값, 원소값)
for idx, tower in enumerate(towers):
    print(idx, tower)

range() 사용하지 않아도 됨, 실수 감소, 숏코딩 가능
'''

# 중요 개념 : stack에서 현재 탑의 높이보다 낮은 것들을 모두 꺼내면, 스택 맨 위에 있는 값이 수신 받는 탑이 됨
# stack이 비었다 -> 현재 탑에서 송신 가능한 탑이 없다

for idx, tower in enumerate(towers):
    while stack and stack[-1][1] <= tower:          # stack이 비어 있지 않고 최상단에 저장된 탑의 높이가, 현재 탑의 높이보다 낮으면
        stack.pop()                                 # stack 최상단에 저장된 탑 정보를 삭제 -> stack이 비어있거나 최상단에 저장된 탑의 높이가, 현재 탑의 높이보다 높거나 같을 때까지 반복

    if stack:                                       # stack이 비어 있지 않으면=> stack의 최상단에 저장된 탑의 높이가 현재 탑의 높이보다 높거나 같으면
        result[idx] = stack[-1][0]                  # result[idx] 값을 stack 최상단에 저장된 탑의 idx+1 값으로 설정

    stack.append((idx + 1, tower))              # stack에 towers(idx)의 탑보다 높거나 같은 것들을 저장

print(*result, sep=' ')
