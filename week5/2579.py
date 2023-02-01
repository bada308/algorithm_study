def Cal(d, stair_list):
    for i in range(3, len(stair_list)):
        # n-1칸을 안 밟았을 때
        if d[i - 1] == d[i - 2]:
            d[i] = d[i - 1] + stair_list[i - 1]
        # n-1칸을 밟았을 때
        else:
            # n-2칸을 안 밟았을 때
            if d[i - 2] == d[i - 3]:
                if stair_list[i] < stair_list[i - 1]:
                    d[i] = d[i - 1] + stair_list[i - 1]
                else:
                    d[i] = d[i - 1]
            # n-2칸을 밟았을 때
            else:
                d[i] = d[i - 1]

    return d


def Solution(stair_list):
    stair_list.reverse()
    stair_list.append(0)

    if len(stair_list) < 3:
        return sum(stair_list)
    else:
        d = [0 for _ in range(len(stair_list) + 1)]
        d[0] = 0
        d[1] = stair_list[0]
        # 경우의 수 두 개
        d[2] = stair_list[0] + stair_list[1]
        result_1 = Cal(d, stair_list)[-2]

        d = [0 for _ in range(len(stair_list) + 1)]
        d[0] = 0
        d[1] = stair_list[0]
        d[2] = stair_list[0]
        result_2 = Cal(d, stair_list)[-2]

    return max(result_1, result_2)

n = int(input())
stair_list = list()
for i in range(n):
    stair = int(input())
    stair_list.append(stair)


print(Solution(stair_list))
# 반례 3 5 10 9 2 1 2 5 2 9, 정답 : 37, 출력 : 33
# 개똥같은 코드.. 첨부터 잘못 만들어버렸다..
