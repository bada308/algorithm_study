# # BJ 2447 / GOLD V /

n = int(input())
copy_n = n
k = int(n / 3)

array = [['*' for i in range(n)] for i in range(n)]


def arr_print():
    for i in array:
        for j in i:
            print(j, end="")
        print()
    print('\n')
    return 0


count = 0
for i in range(copy_n):
    if copy_n % 3 == 0:
        count += 1
        copy_n = copy_n / 3

# print('count:', count)

sqr = []
a = 3
for i in range(count):
    sqr.append(a)
    a *= 3
# print('a: ', sqr)


for i in range(n):
    for j in range(n):
        if i % 3 == 1 & j % 3 == 1:
            array[i][j] = ' '

        elif i // k == 1 & j // k == 1:
            array[i][j] = ' '

        for alpha in sqr:
            for beta in sqr:
                if i % alpha // beta == 1:
                    if j % alpha // beta == 1:
                        array[i][j] = ' '

arr_print()


'''
NOTE:
2차원 배열로 접근한거 나름 괜춘한 방법이라고 생각했는데,,, 왜 시간초과가 나는걸까

여러분 이 코드 버리기 아까워요... 그러니까 일단 이걸로 올리고 금욜 전까지 시간제한 맞춘 코드로 다시 올릴게요

'''