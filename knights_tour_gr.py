import matplotlib.pyplot as plt


def draw_board(size):
    for i in range(size):
        for j in range(size):
            if (j % 2) == (i % 2):
                plt.fill([i, i + 1, i + 1, i], [j, j, j + 1, j + 1], color='gray')
            else:
                plt.fill([i, i + 1, i + 1, i], [j, j, j + 1, j + 1], color='white')

    plt.xlim(0, size)
    plt.ylim(0, size)
    plt.axis('off')


def calculate_knight_moves(start_position, board_size):
    moves = [start_position]
    current_pos = start_position
    possible_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    for _ in range(board_size * board_size - 1):
        valid_moves = []
        for move in possible_moves:
            next_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            if 0 <= next_pos[0] < board_size and 0 <= next_pos[1] < board_size and next_pos not in moves:
                valid_moves.append(next_pos)

        if valid_moves:
            next_pos = min(valid_moves, key=lambda pos: len([
                move for move in possible_moves if (pos[0] - current_pos[0], pos[1] - current_pos[1]) == move
            ]))
            moves.append(next_pos)
            current_pos = next_pos
        else:
            break

    return moves


def draw_knight_moves(size, moves):
    draw_board(size)
    current_pos = moves[0]
    dot(current_pos)

    for i in range(1, len(moves)):
        next_pos = moves[i]
        connect(current_pos, next_pos)
        dot(next_pos)
        current_pos = next_pos
        plt.pause(0.2)

    plt.show()


def connect(pos1, pos2):
    plt.plot([pos1[0] + 0.5, pos2[0] + 0.5], [pos1[1] + 0.5, pos2[1] + 0.5], color='red', linewidth=2)


def dot(pos):
    plt.plot(pos[0] + 0.5, pos[1] + 0.5, 'ro', markersize=4)


# Въвеждане на начална позиция и размер на дъската от потребителя
start_position = (0, 0)
board_size = 6

# Изчисляване на движенията на коня
moves = calculate_knight_moves(start_position, board_size)

# Визуализиране на движенията на коня
draw_knight_moves(board_size, moves)
