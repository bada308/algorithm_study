# BJ 1003 / SILVER III /
import sys

zero = 0
one = 0
numbers = []
result = []
n_list = []
num_table = []

def fibo(n):
    global zero
    global one
    if n == 0:
        zero += 1
    elif n == 1:
        one += 1
    else:
        if n - 1 in n_list:
            zero += num_table[n_list.index(n - 1)][0]
            one += num_table[n_list.index(n - 1)][1]
        else:
            fibo(n-1)

        if n - 2 in n_list:
            zero += num_table[n_list.index(n - 2)][0]
            one += num_table[n_list.index(n - 2)][1]
        else:
            fibo(n-2)

    if n not in n_list:
        n_list.append(n)
        num_table.append((zero, one))


t = int(sys.stdin.readline().strip())

for i in range(t):
    zero = 0
    one = 0

    k = int(sys.stdin.readline().strip())
    fibo(k)
    result.append((zero, one))

for tup in result:
    print(tup[0], tup[1], end='')
    # if result.index(tup) != len(result)-1:
    #     print('')
