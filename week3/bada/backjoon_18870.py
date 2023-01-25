'''
/* 문제 정보 */
18870번 - 좌표 압축
난이도 - 실버 2

/* 풀이 방법 */
1. 입력
2. 몇 종류의 숫자가 있는지 확인
'''
# 1
N = int(input())
input_list = list(map(int, input().split()))

input_list = list(enumerate(input_list))
input_list.sort(key = lambda x:x[1])

answer = []

# 2
cnt = 0

answer.append((input_list[0][0], 0))

for i in range(1, N):
    if(input_list[i][1] != input_list[i-1][1]):
        cnt += 1
    answer.append((input_list[i][0], cnt))


answer.sort(key=lambda x:x[0])

for x, y in answer:
    print(y, end=" ")



'''
/* 오답노트 */

/* 느낀점 */
파이썬이 아닌 언어였으면 정렬이 너무 힘들었을 것 같다.
sort 함수 잘 공부하면 정렬은 잘 할 수 있겠다
여전히 코드가 깔끔하진 않다....
'''