'''
/* 문제 정보 */
14889번 - 스타트와 링크
난이도 - 실버 2

/* 풀이 방법 */


'''
import sys, math

n = int(input())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

member = [i for i in range(1, n+1)]
answer = math.inf

team = []
team2 = []

def team_up():
    global answer

    if len(team) == int(n // 2):
        team2 = [x for x in member if x not in team]
        answer = min(answer, get_power(team, team2))
        return
    
    for i in range(1, n+1):
        if i in team:
            continue
        if len(team) > 0 and i < team[-1]:
            continue
        team.append(i)
        team_up()
        team.pop()

def get_power(t1, t2):
    t1_power = 0
    t2_power = 0

    for i in range(n//2):
        for j in range(i+1, n//2):
            t1_power += (s[t1[i] - 1][t1[j] - 1] + s[t1[j] - 1][t1[i] - 1])

    for i in range(n//2):
        for j in range(i+1, n//2):
            t2_power += (s[t2[i] - 1][t2[j] - 1] + s[t2[j] - 1][t2[i] - 1])

    return abs(t1_power - t2_power)

team_up()

print(answer)

'''
/* 오답노트 */

/* 느낀점 */

'''