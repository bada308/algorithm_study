def factorial(num):
    result = num
    if num == 1 or num == 0:
        return 1
    while 1:
        if num == 1 or num == 0:
            break
        num -= 1
        result *= num

    return result


def permutation(n, r):
    result = factorial(n) // ((factorial(n - r) * factorial(r)))
    return result


a, b = map(int, input().split())
print(permutation(a + b - 1, a) % 1000000000)

# dp 몰랐을 때 풀어놨던 거.. 나중에 dp로 푼거 추가해야겠다 시간이 너무 부족했어...
