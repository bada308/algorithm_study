import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0 for i in range(n)]

for idx, num in enumerate(list(reversed(arr))):
    while stack and stack[-1][1] <= num:
        stack.pop()
    if stack:
        result[idx] = stack[-1][1]
    else:
        result[idx] = -1
    stack.append((idx + 1, num))
print(*list(reversed(result)), sep=' ')