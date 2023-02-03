num = int(input())
num_list = list(map(int, input().split()))

d = [1] * num

tmp_list = [num_list[0]]
smallest_num = num_list[0]

# 부분집합 판별하는 식
for i in range(0, len(num_list)):
    index_num = num_list[i]
    smallest_num = min(smallest_num, num_list[i])
    if num_list[i] > smallest_num:
        continue

    for j in range(i + 1, len(num_list)):
        if num_list[j] > index_num:
            index_num = num_list[j]
            d[j] = max(d[j],  d[j-1] + 1)
        else:
            d[j] = d[j - 1]
    # num_list[i]가 가장 긴 증가하는 부분 수열의 시작점이라고 가정


print(d[-1])

#안풀린다 ㅎ...;
