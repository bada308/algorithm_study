def BT():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if i in result:
            continue
        else:
            result.append(i)
            BT()
            result.pop()
    return


N, M = map(int, input().split())
num_list = list(range(N + 1))
result = []

BT()

"""
재귀는 항상 어렵다....
이것도 어렵다....
"""