def BT():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if not result:
            result.append(i)
            BT()
            result.pop()
        else:
            if i >= max(result):
                result.append(i)
                BT()
                result.pop()

    return


N, M = map(int, input().split())
num_list = list(range(N + 1))
result = []

BT()

"""
앞서 풀었던 두 문제 합친 느낌이라 잘 풀렸다.
"""