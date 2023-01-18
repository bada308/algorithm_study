# BJ 1431 / SILVER III / 152ms
import string
import sys

n = int(sys.stdin.readline().strip())
arr = []


for i in range(n):
    arr.append(sys.stdin.readline().strip())

for i in range(n - 1):
    for j in range(i+1, n):
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

        elif len(arr[i]) == len(arr[j]):
            sum_1, sum_2 = 0, 0
            for x, y in zip(arr[i], arr[j]):
                if x.isdigit():
                    sum_1 += int(x)
                if y.isdigit():
                    sum_2 += int(y)
            if sum_1 > sum_2:
                arr[i], arr[j] = arr[j], arr[i]

            elif sum_1 == sum_2:
                for x, y in zip(arr[i], arr[j]):
                    if x > y:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                    elif x < y:
                        break


print('\n'.join(arr))


'''
NOTE:
i와 j값 범위 설정할 때, i보다 왼쪽에 있는 값은 이미 정렬된 값들이라서 j를 i보다 크게 설정했어야 했는데
i -> (0, n-1) / j -> (1, n) 으로 설정해서 계속 헤맸다...

너무 어렵다
'''