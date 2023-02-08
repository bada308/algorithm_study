'''
/* 문제 정보 */
11729번 - 하노이 탑 이동 순서
난이도 - 실버 1

/* 풀이 방법 */
재귀함수
가장 큰 원판을 목표지점에 두고 그 위에 있는 원판들을 다른 기둥에 옮긴다
'''


def hanoi(num, from_pos, to_pos, other_pos):
    if num == 0: return 0
    global cnt
    global answer
    cnt += 1

    hanoi(num-1, from_pos, other_pos, to_pos)
    answer.append((from_pos, to_pos))
    hanoi(num-1, other_pos, to_pos, from_pos)

N = int(input())
cnt = 0
answer = []

hanoi(N, 1, 3, 2)
print(cnt)
for x, y in answer:
    print(x, y)

'''
/* 오답노트 */
재귀함수는 어렵다.. 유튜브 보고 하노이 탑에서 재귀함수가 사용되는 이유를 이해하고 문제를 풀었다!
전에 풀었던 내 코드는 하노이 탑 공식을 이용해서 출력부를 깔끔하게 작성했다.


def hanoi(num, start, goal, asst):
    if num == 1:
        print(start, goal)
        return
    hanoi(num - 1, start, asst, goal)
    print(start, goal)
    hanoi(num - 1, asst, goal, start)


n = int(input())
print(2**n - 1)

hanoi(n, 1, 3, 2)

/* 느낀점 */

'''