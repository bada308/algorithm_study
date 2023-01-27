# BJ 2156 / SILVER I / 48ms
import sys

n = int(sys.stdin.readline().strip())
nums = [0]

for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

d = [0] * (n + 1)

if n == 1:
    d[1] = nums[1]
    print(d[1])

elif n == 2:
    d[2] = nums[1] + nums[2]
    print(d[2])

else:
    for i in range(3, n+1):
        d[1] = nums[1]
        d[2] = nums[1] + nums[2]
        d[i] = max(d[i - 1], max(d[i - 2] + nums[i], d[i - 3] + nums[i - 1] + nums[i]))
    print(d[n])


'''
NOTE:
이 문제는 레전드 어려움이었음
감도 안왔다!! 알고리즘 수업을 안들어서 그런가 a[i] - d[i] 표 만들어서 점화식 세우는 게 익숙하지가 않았다
규칙 찾아봤는데도 이해하는 데 시간이 꽤 걸린 문제....

이해하고 코드를 작성하는데 마지막 조건문에서
d[1] = nums[1]
d[2] = nums[1] + nums[2]
를 빠뜨려서 계속 틀렸습니다 떴음 ㅠㅠ

처음부터 디버깅했으면 바로 확인할 수 있었을텐데!! 디버깅 습관들여야겠다~~ 휴

'''