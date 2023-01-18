'''
/*문제 정보 */
11729번 - 하노이 탑 이동 순서
난이도 - 실버 1

/*풀이 방법 */
하노이탑 최소 이동 횟수는 2**n -1번
하노이탑 알고리즘 단계를 3개로 나눴다.
1단계는 n-1개의 원판을 1번 막대기에서 2번 막대기로 옮긴다.
2단계는 1개의 원판을 1번 막대기에서 3번 막대기로 옮긴다.
3단게는 n-1개의 원판을 2번 막대기에서 3번 막대기로 옮긴다.
'''
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return

    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계

n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
'''
/*오답 노트*/
/*느낀 점*/
이 문제를 풀기 위해 하노이탑을 이해하는게 시작이었다.
이해를 해도 코딩으로 적용하는데 너무 힘들다다다다다다다.
'''