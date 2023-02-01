# BJ 1932 / SILVER I / 152ms
import sys

n = int(sys.stdin.readline().strip())

nums = []

for i in range(n):
    nums.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            nums[i][0] += nums[i - 1][0]
        elif j == i:
            nums[i][j] += nums[i - 1][j - 1]
        else:
            nums[i][j] += max(nums[i - 1][j - 1], nums[i - 1][j])

print(max(nums[n-1]))



'''
NOTE:
아 다이나믹 프로그래밍 진짜 어렵다!!!!!!!!!

규칙은 찾았는데...... 식으로 표현하는 게 장난 아니게 어렵다
먼가.. 아래에서 위로 올라가는 방향으로 짜면 더 나을 것 같았는데 더 어려워짐ㅠ

코딩하는데 필기할 게 필요하다는 거.. 진짜 웃김

'''