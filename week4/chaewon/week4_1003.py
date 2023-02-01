# BJ 1003 / SILVER III / 40ms
import sys

num_table = [(1, 0), (0, 1), (1, 1)]        # (zero, one) tuple 저장


def fibo(t):
    if t >= len(num_table):
        for i in range(len(num_table), t + 1):
            num_table.append((num_table[i-1][0] + num_table[i-2][0], num_table[i-1][1] + num_table[i-2][1]))
    print('{} {}'.format(num_table[t][0], num_table[t][1]))


t = int(sys.stdin.readline().strip())

for j in range(t):
    fibo(int(input()))


'''
NOTE:
다이나믹 프로그래밍 자체가 너무 생소했다
찾아보니까 재귀함수를 쓸 때 불필요하게 소모되는 시간이나 메모리를 막기 위해서
반복되는 값들을 미리 저장해두고 꺼내 쓰는 개념이던데 굉장히 좋은 것 같다

근데 맨날 재귀함수만 써봐서 익숙하지가 않다...

답지에서는 zero와 one을 각각 리스트로 분리했는데 나는 그냥 튜플로 num_table 하나에 저장했다
그렇게 하니까 소요시간이 미세하지만 줄어들었다 신기해! 왤까요??? 그냥 매 실행마다 달라지는 차이인건가
파이썬 자료형별 시간복잡도 찾아봤는데 잘 모르겠다 더 공부해봐야지...
'''