'''
/* 문제 정보 */
1003번 - 피보나치 함수
난이도 - 실버3

/* 풀이 방법 */


'''
t = int(input())
 
for _ in range(t):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
    print(cnt_0[n], cnt_1[n])
    