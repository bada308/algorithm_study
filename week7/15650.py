def BT():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if i not in result:
            if not result:
                result.append(i)
                BT()
                result.pop()
            else:
                if i > max(result):
                    result.append(i)
                    BT()
                    result.pop()
    return


N, M = map(int, input().split())
num_list = list(range(N + 1))
result = []

BT()

"""
15649문제를 이용해서 풀었다.
중복을 피하려면 result에 있는 숫자보다 작은 숫자는 추가하면 안된다.
#13번째 줄
생각해보니 result[-1]이 가장 큰 숫자이므로 max(result) 대신 result[-1]을 써도 될 것 같다.
다른 사람들은 어떻게 풀었을까 봤더니 매개변수로 for문 시작 숫자를 넘겨주면 됐네... 그 코드가 더 나은 듯...ㅠ
"""