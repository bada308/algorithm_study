'''
백준에 올라와있는 예제는 잘 되는데 채점 돌리면 런타임 에러가 떠요ㅠㅠ
혹시 반례 찾으실 수 있는 분은 댓글로 달아주시면 감사하겠습니당
'''

import sys

t = int(sys.stdin.readline())                       # 테스트 케이스의 개수 입력 받기
result = []

for i in range(t):
    func_arr = list(sys.stdin.readline().strip())                                           # R과 D의 배열 입력 받아 list에 저장
    num_arr_size = int(sys.stdin.readline())                                                # 입력할 숫자 배열의 길이

    if num_arr_size != 0:
        num_str = sys.stdin.readline().strip().replace("[", "").replace("]", "")                # 숫자 배열을 입력 받고, [과 ] 제거
        num_arr = list(map(int, num_str.split(',')))                                            # ','를 기준으로 분리, 리스트로 저장
    elif num_arr_size == 0:                                                                   # num_arr_size = 0이면 num_str을 ','로 split하는 과정에서 오류 발생 -> 예외 처리
        num_arr = sys.stdin.readline().strip().replace("[", "").replace("]", "")

    for j in range(len(func_arr)):
        if func_arr[j] == 'R':
            num_arr = num_arr[::-1]
            if num_arr_size == 0:
                num_arr = []

        elif func_arr[j] == 'D':
            if num_arr_size == 0:
                num_arr = 'error'
            else:
                num_arr.pop(0)

    result.append('['+','.join(map(str, num_arr))+']')

print(*result, sep='\n')