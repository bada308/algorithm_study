import sys


# 아이디어 : numbers에 있는 숫자를 하나씩 stack에 넣고 다음 숫자와 비교


n, k = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline().rstrip()
stack = []

for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))