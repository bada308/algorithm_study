'''
/* 문제 정보 */
2156번 - 포도주 시식
난이도 - 실버1

/* 풀이 방법 */


'''
wine = int(input())
wine_capa = [0]
result = [0 for _ in range(wine + 1)]

for _ in range(wine):
    wine_capa.append(int(input()))

for i in range(1, wine + 1):
    if i == 1:
        result[1] = wine_capa[1]
    elif i == 2:
        result[2] = wine_capa[1] + wine_capa[2]
    else:
        result[i] = max(result[i-3] + wine_capa[i-1] + wine_capa[i], result[i-2] + wine_capa[i], result[i-1])  

print(result[i])