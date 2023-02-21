# BJ 17478 / Silver V / 36ms


def recursion(k):
    bar = '____'
    if k == 0:
        print(bar * (n - k) + "\"재귀함수가 뭔가요?\"")
        print(bar * (n - k) + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(bar * (n - k) + '라고 답변하였지.')
        return 0
    else:
        print(bar * (n - k) + "\"재귀함수가 뭔가요?\"")
        print(bar * (n - k) + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(bar * (n - k) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(bar * (n - k) + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recursion(k - 1)
    print(bar * (n - k) + '라고 답변하였지.')



n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

recursion(n)



'''
NOTE :
문제의 핵심이 under bar를 회귀 횟수만큼 출력하는 것인 듯 한데... 못하겠어서 결국 구글링해서 보면서 했다
간단하게 n-k 곱해주면 되는데 이걸 생각 못한 게 슬푸다

또 n = 0일 때에도 출력해야 하는 문장이 있는데 이 포인트도 놓쳤다
네? 그럼 혼자 한게 뭐냐고요? 몰라요
'''