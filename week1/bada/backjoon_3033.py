# 3003번: 킹, 퀸, 룩, 비숍, 나이트, 폰
# 
# code

king, queen, rook, bishop, knight, pawn = map(int, input().split())
print(1-king, 1-queen, 2-rook, 2-bishop, 2-knight, 8-pawn)