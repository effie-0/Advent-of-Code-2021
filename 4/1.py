def one_around(num, boards, marked, boards_num, square_size):
    for i in range(boards_num):
        for j in range(square_size):
            for k in range(square_size):
                if boards[i][j][k] == num:
                    marked[i][j][k] = True
    
    winner = check_winner(marked, boards_num, square_size)
    return winner


# -1 if there is no winner
def check_winner(marked, boards_num, square_size):
    for i in range(boards_num):
        # check horizontally
        for j in range(square_size):
            result = True
            for k in range(square_size):
                if not marked[i][j][k]:
                    result = False
                    break
            if result:
                return i

        # check vertically
        for j in range(square_size):
            result = True
            for k in range(square_size):
                if not marked[i][k][j]:
                    result = False
                    break
            if result:
                return i
    
    # no winner
    return -1


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        marked_num = []
        boards = []
        board = []
        for line in f.readlines():
            if len(marked_num) == 0:
                marked_num = line.strip().split(',')
            else:
                if len(line.strip()) == 0:
                    if len(board):
                        boards.append(board)
                        board = []
                else:
                    board.append(line.strip().split())
        
        marked_num = [int(x) for x in marked_num]
        boards = [[[int(x) for x in line] for line in board] for board in boards]
        
        boards_num = len(boards)
        square_size = len(boards[0])
        marked = [[[False] * square_size for i in range(square_size)] for j in range(boards_num)]
        
        for num in marked_num:
            result = one_around(num, boards, marked, boards_num, square_size)
            if result != -1:
                remain = 0
                for i in range(square_size):
                    for j in range(square_size):
                        if not marked[result][i][j]:
                            remain += boards[result][i][j]
                print(num, remain, num * remain)
                break
