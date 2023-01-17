'''
/* 문제 정보 */
2447번 - 별 찍기 10
난이도 - 골드 5

/* 풀이 방법 */
공간을 3군데로 나눈 후 재귀함수를 통해 구해진 별을 append 한다.
'''

import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))

'''
/* 오답노트 */
이전 코드도 똑같은 것보니 10달 전에도 어려워서 구글링을 한 것 같다

/* 느낀점 */
재귀적으로 생각하는 사고가 형성이 안 되어 있어서 재귀 문제가 넘넘 어렵다 ㅡㅠ
문제를 더 풀어볼 필요가 있어보임
'''