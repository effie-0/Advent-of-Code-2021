def one_around(num, boards, marked, winners, boards_num, square_size):
    for i in range(boards_num):
        if i in winners:
            continue
        for j in range(square_size):
            for k in range(square_size):
                if boards[i][j][k] == num:
                    marked[i][j][k] = True
    
    check_winner(marked, winners, boards_num, square_size)


# -1 if there is no winner
def check_winner(marked, winners, boards_num, square_size):
    for i in range(boards_num):
        if i in winners:
            continue

        # check horizontally
        is_winner = False
        for j in range(square_size):
            result = True
            for k in range(square_size):
                if not marked[i][j][k]:
                    result = False
                    break
            if result:
                winners.append(i)
                is_winner = True
                break
        
        if is_winner:
            continue

        # check vertically
        for j in range(square_size):
            result = True
            for k in range(square_size):
                if not marked[i][k][j]:
                    result = False
                    break
            if result:
                winners.append(i)
                break


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
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
        
        winners = []
        last_num = -1
        for num in marked_num:
            one_around(num, boards, marked, winners, boards_num, square_size)
            if len(winners) == boards_num:
                last_num = num
                break

        remain = 0
        result = winners[-1]
        for i in range(square_size):
            for j in range(square_size):
                if not marked[result][i][j]:
                    remain += boards[result][i][j]
        print(last_num, remain, last_num * remain)
