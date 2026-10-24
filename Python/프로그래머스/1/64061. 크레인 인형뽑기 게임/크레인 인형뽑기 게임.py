def solution(board, moves):
    answer = 0
    basket = []
    for col in moves:
        for idx,row in enumerate(board):
            if board[idx][col-1] != 0:
                basket.append(board[idx][col-1])
                board[idx][col-1] = 0
                break
    while basket:
        find = False
        pre = basket[0]
        for i in range(1,len(basket)):
            if pre == basket[i]:
                basket = basket[:i-1] + basket[i+1:]
                find = True
                answer += 2
                break
            else:
                pre = basket[i]
        if not find:
            break
    return answer