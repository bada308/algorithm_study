'''
/* 문제 정보 */
5430번 - AC
난이도 - 골드 5
알고리즘 분류 : 자로구조, 문자열, 파싱, 덱

/* 풀이 방법 */
1. 뒤집기 여부를 나타내는 bool 생성
2. 덱을 이용해 뒤집기 여부에 따라 버리기 수행
2.1. 뒤집기 true -> pop()
2.2. 뒤집기 false -> popleft()
3. 출력
3.1. 뒤집기 true -> 앞에서부터 출력
3.2. 뒤집기 false -> 뒤에서부터 출력

'''
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    isReverse = False
    isError = False

    input_list = input()
    input_list = list(map(int, input_list[1:len(input_list)-1].split(','))) if len(input_list) > 2 else []
    input_deque = deque(input_list)

    for i in p:
        if(i == 'R'):
            isReverse = not isReverse
        else:
            try:
                if(isReverse):
                    input_deque.pop()
                else:
                    input_deque.popleft()
            except:
                isError = True
                break


    if(not isError): # 오답노트
        if(isReverse):
            input_deque.reverse()
        print('['+','.join(map(str, input_deque))+']')
    else:
        print("error")



'''
/* 오답노트 */
출력 형식 Error!

입출력 양식은 공백의 유무까지 정확하게 고려해야 합니다. 
예제 입출력을 확인해 보세요. 배열의 수들 사이에는 공백이 없으며, 
입력받을 때 공백이 있어야만 입력받을 수 있는 방밥을 쓰거나 출력할 때 임의로 공백을 삽입해서 출력하면 안 됩니다. 
대표적인 예시로, Python에서 print(list)를 하면 원소들 사이에 불필요한 공백이 출력되어 틀립니다.

/* 느낀점 */
이 문제도 알고리즘 분류의 힌트를 받고 풀었다. 덱을 이용한 문제는 처음이었으며 우선순위 큐와 마찬가지로 구현을 하면서 더 익혀보고 싶다.
입출력 양식도 자세히 봐야한다는 교훈을 얻었다.
'''