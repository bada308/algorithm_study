'''
/* 문제 정보 */
1431번 - 시리얼 번호
난이도 - 실버 3

/* 풀이 방법 */
파이썬 정렬 함수 key=lambda를 이용해서 우선순위를 정해주고 정렬


'''
import re

N = int(input())
serial_list = [input() for _ in range(N)]

for index in range(N):
    serial_len = len(serial_list[index])
    serial_num = re.sub(r'[^0-9]', '', serial_list[index])
    serial_sum = sum([int(i) for i in serial_num])
    serial_list[index] = (serial_list[index], serial_len, serial_sum)

serial_list.sort(key= lambda x :(x[1], x[2], x[0]))
for j in range(N):
    print(serial_list[j][0])

'''
/* 오답노트 */
맞았는데 코드가 세상 지저분해서 다른 사람들 코드를 봐봤다.
내 코드 중에 제일 정리가 안 됐던, 시리얼 번호에서 숫자 추출해서 더하는 과정을 함수로 따로 빼니까 깔끔하다.
직접 각 sort를 구현하는 게 연습할 때는 더 도움이 되는 것 같아서 연습해야겠다.


n = int(input())

arr = []
for i in range(n):
    a = input()
    arr.append(a)


for i in range(n-1):
    for j in range(i+1, n):
        # 짧은 것이 먼저
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

        elif len(arr[i]) == len(arr[j]):
            suma=0
            sumb=0
            for x,y in zip(arr[i],arr[j]):
                if x.isdigit():
                    suma+=int(x)
                if y.isdigit():
                    sumb+=int(y)
            if suma > sumb:
                arr[i],arr[j] = arr[j], arr[i]

            elif suma == sumb:
                for x,y in zip(arr[i], arr[j]):
                    if x > y:
                        arr[i],arr[j] = arr[j], arr[i]
                        break
                    elif x < y:
                        break


for i in arr:
    print(i)

/* 느낀점 */
복잡하면 함수 따로 빼서!
'''