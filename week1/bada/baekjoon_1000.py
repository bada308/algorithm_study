# 1000번: A+B

# 개념
"""
입력 : input
split를 이용해 여러 개 입력받기
int로 변환해줘야 하는데 일일이 변환하기 귀찮으니까 map 합수를 이용해 한 번에 변환
"""
# code
a, b = map(int, input().split())
print(a+b)