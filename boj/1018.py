import copy

def check_8x8(board, start):
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]

    count = 0
    if board[1][1] != start:
        board[1][1] = start
        count += 1
    
    for i in range(1, 9):
        for j in range(1, 9):
            for x, y in zip(d_x, d_y):
                if board[i][j] == board[i + x][j + y]:
                    if board[i][j] == 'B':
                        board[i + x][j + y] = 'W'
                        count += 1
                    elif board[i][j] == 'W':
                        board[i + x][j + y] = 'B'
                        count += 1
    return count


def solve():
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    
    head_point = []
    change = []
    
    for x in range(N - 8 + 1):
        for y in range(M - 8 + 1):
            head_point.append([x, y])
    
    for x, y in head_point:
        board = []
        board.append(['X']*10)
        for i in range(8):
            board.append(['X'] + matrix[x + i][y:y+8] + ['X'])
        board.append(['X']*10)

        change.append(check_8x8(copy.deepcopy(board), 'B'))
        change.append(check_8x8(copy.deepcopy(board), 'W'))
    
    return min(change)

if __name__ == '__main__':
    print(solve())
