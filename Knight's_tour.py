def knights_tour(start, size):
    def is_valid_move(x, y, size, board):
        if x >= 0 and x < size and y >= 0 and y < size and board[y][x] == -1:
            return True
        return False

    def count_valid_moves(x, y, board):
        count = 0
        for i in range(8):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if is_valid_move(next_x, next_y, size, board):
                count += 1
        return count

    def knight_tour_util(x, y, move_count, board, move_x, move_y, path):
        board[y][x] = move_count
        path.append((x, y))

        if move_count == size * size:
            return True

        possible_moves = []
        for i in range(8):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            if is_valid_move(next_x, next_y, size, board):
                count = count_valid_moves(next_x, next_y, board)
                possible_moves.append((next_x, next_y, count))

        possible_moves.sort(key=lambda move: count_valid_moves(move[0], move[1], board))

        for move in possible_moves:
            next_x, next_y, _ = move
            if knight_tour_util(next_x, next_y, move_count + 1, board, move_x, move_y, path):
                return True

        board[y][x] = -1
        path.pop()

        return False

    board = [[-1 for _ in range(size)] for _ in range(size)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    start_x, start_y = start
    board[start_y][start_x] = 0
    path = []

    knight_tour_util(start_x, start_y, 1, board, move_x, move_y, path)
    return path


# Пример за използване на функцията knights_tour
start_position = (0, 0)
board_size = 6
path = knights_tour(start_position, board_size)
print(f"Starting on: {start_position}")
print("Path:")
for point in path:
    print(point)
