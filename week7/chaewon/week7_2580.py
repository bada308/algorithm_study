# BJ 2580 : 스도쿠 / GOLD IV

import sys


def check_row(x, n):
    for i in range(9):
        if n == board[x][i]:
            return False
    return True


def check_col(y, n):
    for i in range(9):
        if n == board[i][y]:
            return False
    return True


def check_sqr(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == board[nx + i][ny + j]:
                return False
    return True


def sudoku(n):
    if n == len(blank):
        for k in range(9):
            print(*board[k])
        exit(0)

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if check_row(x, i) and check_col(y, i) and check_sqr(x, y, i):
            board[x][y] = i
            sudoku(n + 1)
            board[x][y] = 0


board = []
blank = []

for i in range(9):
    board.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])

sudoku(0)


'''
NOTE:
처음에 행 단위로 0 여부 검사 후 1~9 넣는건 성공했는데,
3x3 정사각형 단위로 검사하는 게 너무 어려웠다ㅠ

2차원 배열인 board를 3x3으로 슬라이싱해서 새로운 리스트로 저장했었는데,
그러니까 현재 좌표에서 이 새로운 리스트로의 접근이 어려워졌다...

코드 찾아보니까, 3x3 행렬에서 (0, 0)좌표에 해당하는 점을 (nx, ny)로 받아오던데
이런건 정말 많이 풀어봐야 느는 사고인 것 같다
나도 몫이나 나머지로 접근해보려고 시도는 했었는데 방법을 못찾았다ㅠ
그리고 또 나는 (0, 0)이 아니라 (1, 1), 그러니까 3x3행렬의 중앙값을 가져오려고 했었다

아 어렵다!!

+ pypy로 제출해야 시간 초과가 안뜬다ㅠ
찾아보니까 해당 문제가 특히 python으로 시간 초과 안내기가 어렵다는 듯..? 잘 모르겠다
pypy는 실행시 자주 쓰이는 코드를 캐싱하는 기능이 있어서
"복잡하거나 반복되는 코드"를 사용한 경우에는 pypy를 사용하는 것이 메모리와 속도 측에서 낫다

'''