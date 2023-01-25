'''
/* 문제 정보 */
1932번 - 정수 삼각형
난이도 - 실버1

/* 풀이 방법 */


'''
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().split())))
 
for i in range(1,n):
    for j in range(len(li[i])):
        if j==0:
            li[i][j] += li[i-1][0]
        elif j==len(li[i])-1:
            li[i][j]+=li[i-1][-1]
        else:
            li[i][j] += max(li[i-1][j],li[i-1][j-1])
            
print(max(li[-1]))

    