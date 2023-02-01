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
# print('sqr: ', sqr)


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
<<<<<<< HEAD
여러분 저는 이 소중한 제 코드를 버릴 수 없어요
죄송한데 이 문제는 이걸로 제출하고 구글링해서 다른 방법도 알아볼게욤 ㅎㅣ히
=======

여러분 이 코드 버리기 아까워요... 그러니까 일단 이걸로 올리고 금욜 전까지 시간제한 맞춘 코드로 다시 올릴게요
>>>>>>> fbd3deaa275edcdb0a5a5a937deb4de146ea4e39

'''