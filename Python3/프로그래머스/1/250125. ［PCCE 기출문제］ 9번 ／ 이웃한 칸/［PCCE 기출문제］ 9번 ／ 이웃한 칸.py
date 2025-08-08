from collections import Counter
def solution(board, h, w):
    ad = []
    if h > 0: # 위
        ad.append(board[h-1][w])
    if h < (len(board)-1): # 아래
        ad.append(board[h+1][w])
    if w > 0: # 왼쪽
        ad.append(board[h][w-1])
    if w < (len(board[0])-1): # 오른쪽
        ad.append(board[h][w+1])
    return Counter(ad)[board[h][w]]