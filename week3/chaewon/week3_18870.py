# BJ 18870 / SILVER II / 1920ms
import sys

n = int(sys.stdin.readline().strip())
result = []

numbers = list(map(int, input().split(' ')))

a = sorted(set(numbers))                    # 중복제거 후 정렬된 리스트

num_dict = {}
for i in range(len(a)):                     # 핵심 아이디어 : dict 만들어서, "키:값"을 "숫자:인덱스" 로 표현
    num_dict[a[i]] = i                      # 정렬되어 있기 때문에 인덱스 값이 "자신보다 작은 수의 개수(결과값)"에 해당함

for i in numbers:                           # numbers(처음 입력받은 리스트) 순서에 맞춰서, 이 숫자를 키로 사용해서 딕셔너리에서 value(인덱스) 불러와서 출력
    print(num_dict[i], end=' ')
