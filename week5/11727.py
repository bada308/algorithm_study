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


def Cal_factorials(list_one_two):
    num_two = list_one_two.count(2)
    num_one = list_one_two.count(1)

    # // -> / 로 바꾸면 안됨..?
    result = factorial(len(list_one_two)) // ((factorial(num_two) * factorial(num_one)))

    return result


num = int(input())

num_list = [2 for i in range(num // 2)]
if num % 2 != 0:
    num_list.append(1)

result = 0
while 1:
    result += Cal_factorials(num_list)*(2**num_list.count(2))
    if 2 in num_list:
        num_list.remove(2)
        num_list.append(1)
        num_list.append(1)
    else:
        break

print(result % 10007)
# dp 몰랐을 때 풀어놨던 거.. 나중에 dp로 푼거 추가해야겠다 시간이 너무 부족했어...