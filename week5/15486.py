N = int(input())

T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
d = [0 for _ in range(N + 1)]

for i in range(N):
    T_num, P_num = map(int, input().split())
    T[i] = T_num
    P[i] = P_num

if T[0] == 1:
    d[1] = P[0]



for i in range(2, N + 1):
    tmp_list = list()
    for j in range(i - 1, 0, -1):
        tmp_1 = j + T[j]
        tmp_2 = i
        if j + T[j] == i:
            tmp_list.append(P[j])
    if tmp_list:
        d[i] = d[i-1] + max(tmp_list)
    else:
        if d[i-1] != 0:
            d[i] = d[i - 1]


print(d[-1])

# 좀만 고치면 될 거 같은데 시간이 없어서 일단 올림....ㅠㅠㅠㅠㅠ