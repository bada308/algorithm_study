N = int(input())

T = [0 for _ in range(N)]
P = [0 for _ in range(N)]
d = [0 for _ in range(N)]

for i in range(N):
    T_num, P_num = map(int, input().split())
    T[i] = T_num
    P[i] = P_num

if T[0] == 1:
    d[0] = P[0]

for i in range(1, N):
    tmp_list = list()
    for j in range(i, -1, -1):
        tmp_1 = j + T[j]
        tmp_2 = i
        if j + T[j] - 1 == i:
            tmp_list.append(P[j] + d[j-1])
    if tmp_list:
        d[i] = max(tmp_list)
    else:
        if d[i-1] != 0:
            d[i] = d[i - 1]



print(d[-1])

# 고쳤는데 시간 초과 떠서 시간 어떻게 줄일지 찾아봐야겠다..
