# BJ 2193 / SILVER III / 40ms

result = [0, 1, 1]


def pinary(n):
    if n >= len(result):
        for i in range(len(result), n + 1):
            result.append(result[i-1] + result[i-2])
    print(result[n])


n = int(input())
pinary(n)


'''
NOTE:
1003과 비슷한 문제인 것 같았는데, 규칙을 못찾았다ㅠ
굳이굳이 이진수 생성하려고 난리치다가 결국 답지 보고 풀이...
다이나믹 프로그래밍의 핵심은 규칙 찾기인 것 같다
'''