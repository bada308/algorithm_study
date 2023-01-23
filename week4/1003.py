'''
/*문제 정보 */
1003번 - 피보나치 함수
난이도 - 실버 3

/*풀이 방법 */
잘 알려진 피보나치수열에 zero, one 변수를 만들어 매번 카운트 하는 식으로 한다.
라고 했더니 시간 초과 .....
고민 끝에 서치해 본 결과 0 과 1 리턴하는 형태도 피보나치 형태인 것을 확인
zero, one 리스트로 만들어서 피보나치 이용 했다..
'''
def fibonacci(n):
  zero = [1, 0, 1]
  one = [0, 1, 1]
  if len(zero) <= n:
    for i in range(len(zero), n+1):
      zero.append(zero[i-2]+zero[i-1])
      one.append(one[i-2]+one[i-1])
  return zero[n], one[n]

N = int(input())

for i in range(N):
  n = int(input())
  a, b = fibonacci(n)
  print(a, b)
'''
/*오답 노트*/
def fibonacci(n):
    global zero
    global one
    if n == 0 :
        zero += 1
        return 0

    elif n ==1 :
        one += 1
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input())

for i in range(a):
    n = int(input())
    zero = 0
    one = 0
    fibonacci(n)
    print(zero, one)
반복문을 쓰면 시간 초과가 뜬다... 
/*느낀 점*/
처음 문제보고 제한 시간이 엄청 짧은 걸 보고 생각했어야 했는데..
하여튼 문제 한번에 푸는 사람들 신기해...
'''