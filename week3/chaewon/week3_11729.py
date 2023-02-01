# BJ 11729 / Silver I / 896ms

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6 - start - end)            # 6 - start - end: 중간에 거쳐야만 하는 기둥의 번호
    print(start, end)
    hanoi(n - 1, 6 - start - end, end)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)

'''
NOTE:
하노이탑 start -> end 으로 원판 n개를 옮기기 위해서는
중간 과정이 꼭 필요 : 처음과 끝 모두에 해당하지 않는 막대에 가장 크기가 큰 원판을 제외한 n-1개의 원판을 옮겨야 함
그 다음에서야 중간 과정 막대 -> end 막대로 옮길 수 있음

전체 횟수는 공식 : 2**n - 1
'''