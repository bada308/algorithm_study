# BJ 11729 / Silver I /
n = int(input())

first = [(i+1) for i in range(n)]
second = []
third = []

for i in range(n):
    f_pop = first.pop()
    if len(second) != 0 and f_pop < second[-1]:
        second.append(f_pop)
    elif not len(second):
        second.append(f_pop)

