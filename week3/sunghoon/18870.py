'''
/*문제 정보 */
18870번 - 좌표 압축
난이도 - 실버 2

/*풀이 방법 */
set으로 중복되는 값을 없애주고 정렬시켜준다.
그 후 인덱스값을 나타내게 한다.
'''
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
new_a = sorted(set(a))
dictionary = {new_a[i]: i for i in range(len(new_a))}

for i in a:
    print(dictionary[i], end=' ')
'''
/*오답 노트*/
/*느낀 점*/
이 문제를 통해 input() 대신에 sys.stdin.readline 사용해 시간초과를 방지하는 것을 배웠다..!

'''