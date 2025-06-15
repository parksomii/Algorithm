def solution(keyinput, board):
    x, y = 0, 0  # 시작 위치
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    for key in keyinput:
        if key == "left" and x > -x_limit:
            x -= 1
        elif key == "right" and x < x_limit:
            x += 1
        elif key == "up" and y < y_limit:
            y += 1
        elif key == "down" and y > -y_limit:
            y -= 1

    return [x, y]