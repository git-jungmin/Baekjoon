def solution(m, n, board):
    board = [list(i) for i in board]
    answer = 0
    while True:
        block = set()
        # 4블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    block.update({(i,j),(i,j+1),(i+1,j),(i+1,j+1)})
        if not block:
            break
        # 블록 제거
        for i,j in block:
            board[i][j] = ''
            answer += 1
        # 블록 낙하
        for i in range(n):
            empty = []
            for j in range(m-1,-1,-1):
                if empty and board[j][i] != '':
                        a,b = empty.pop(0)
                        board[a][b] = board[j][i]
                        board[j][i] = ''
                if board[j][i] == '':
                    empty.append((j,i))
    return answer