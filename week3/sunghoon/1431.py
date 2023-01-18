'''
/*문제 정보 */
1431번 - 시리얼 번호
난이도 - 실버 3

/*풀이 방법 */
정렬 기준은 길이, 숫자합, 사전순!
길이, 사전순은 lambda에 넣으면 되지만 숫자합은 그렇지 않기 때문에 함수로 따로 작성
'''
def sum(n):
    count = 0
    for i in n:
        if i.isdigit():
            count += int(i)
    return count

a = int(input())
b = []
for i in range(a):
    b.append(input())

b.sort(key=lambda x:(len(x), sum(x),x))
for i in b:
    print(i)
'''
/*오답 노트*/
/*느낀 점*/
아직 너무 힘들다.... 계속 연습하다보면 되지 않을까...
그래도 모르는 함수, 기능 계속 검색하면서 공부하니까 꽤나 많이 알아가는거 같다..
'''