def solution(board):
    danger = set()
    directions = [(-1,-1),(-1,0),(0,-1),(-1,1),(0,1),(1,0),(1,-1),(1,1)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                danger.add((i,j))
                for dx,dy in directions:
                    nx, ny = dx + i, dy + j
                    if 0 <= nx < len(board) and 0 <= ny < len(board):
                        danger.add((nx,ny))
    return len(board)**2 - len(danger)