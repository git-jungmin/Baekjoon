def solution(keyinput, board):
    x,y = 0,0
    x_range = board[0] // 2
    y_range = board[1] // 2
    for i in keyinput:
        if i == "left" and x > -x_range:
            x -= 1
        elif i == "right" and x < x_range:
            x += 1
        elif i == "up" and y < y_range:
            y += 1
        elif i == "down" and y > -y_range:
            y -= 1
    return [x,y]