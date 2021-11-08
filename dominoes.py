import random

domino_set = []
for i in range(0, 7):
    for j in range(i, 7):
        domino_set.append([i, j])
del i, j
domino_snake = []
status = None
turn = None
game_over = False


def print_snake(snake):
    if len(snake) < 7:
        for stone in snake:
            if stone == snake[0] and len(snake) == 1 or stone == snake[-1]:
                print(stone)
            else:
                print(str(stone), end=', ')
    else:
        print(f'{snake[0]}, {snake[1]}, {snake[2]}...{snake[-3]}, {snake[-2]},'
              f' {snake[-1]}')


while not turn:
    random.shuffle(domino_set)
    stock_pieces = domino_set[0:14]
    computer_pieces = domino_set[14:21]
    player_pieces = domino_set[21:28]
    computer_doubles = [stone for stone in computer_pieces
                        if stone[0] == stone[1]]
    player_doubles = [stone for stone in player_pieces
                      if stone[0] == stone[1]]
    if len(computer_doubles) == 0 and len(player_doubles) == 0:
        continue
    if len(computer_doubles) == 0:
        turn = 'computer'
        domino_snake.append(max(player_doubles))
        player_pieces.remove(max(player_doubles))
        break
    elif len(player_doubles) == 0:
        turn = 'player'
        domino_snake.append(max(computer_doubles))
        computer_pieces.remove(max(computer_doubles))
        break
    if max(computer_doubles) > max(player_doubles):
        turn = 'player'
        domino_snake.append(max(computer_doubles))
        computer_pieces.remove(max(computer_doubles))
    else:
        turn = 'computer'
        domino_snake.append(max(player_doubles))
        player_pieces.remove(max(player_doubles))


def reorient_stone(stone):
    a = stone[0]
    stone[0] = stone[1]
    stone[1] = a
    return stone


def check_move(stone, side):
    if side == 'left':
        return domino_snake[0][0] in stone
    elif side == 'right':
        return domino_snake[-1][1] in stone


def print_display():
    global stock_pieces
    global computer_pieces
    global player_pieces
    global domino_snake
    print('=' * 70)
    print('Stock size: ' + str(len(stock_pieces)))
    print('Computer pieces: ' + str(len(computer_pieces)) + '\n')
    print_snake(domino_snake)
    print('\nYour pieces:')
    if player_pieces:
        for i in range(len(player_pieces)):
            print(f'{i + 1}:{player_pieces[i]}')
    print()


while not game_over:
    print_display()
    if len(player_pieces) == 0:
        status = 'Status: The game is over. You won!'
        game_over = True
        break
    elif len(computer_pieces) == 0:
        status = 'Status: The game is over. The computer won!'
        game_over = True
        break
    # The numbers on the ends of the snake are identical and appear within the
    # snake 8 times. No side will have a stone to play. It's a draw.
    if domino_snake[0][0] == domino_snake[-1][0]:
        count = 0
        for stone in domino_snake:
            if stone[0] == domino_snake[0][0]:
                count += 1
            if stone[1] == domino_snake[0][0]:
                count += 1
        if count >= 8:
            status = 'Status: The game is over. It\'s a draw!'
            game_over = True
            break
    if turn == 'computer':
        turn = 'player'
        input_checked = False
        input('Status: Computer is about to make a move. Press Enter to '
              'continue...\n')
        while not input_checked:
            try:
                move = random.randint(
                    (len(computer_pieces) * -1),
                    len(computer_pieces))
                stone = computer_pieces[abs(move)]
                if move < 0:
                    if check_move(stone, 'left'):
                        computer_pieces.remove(stone)
                        if domino_snake[0][0] != stone[1]:
                            stone = reorient_stone(stone)
                        domino_snake.insert(0, stone)
                        input_checked = True
                    else:
                        continue
                elif move == 0:
                    if len(stock_pieces):
                        stone = random.choice(stock_pieces)
                        stock_pieces.remove(stone)
                        computer_pieces.append(stone)
                    input_checked = True
                elif move > 0:
                    if check_move(stone, 'right'):
                        computer_pieces.remove(stone)
                        if domino_snake[-1][1] != stone[0]:
                            stone = reorient_stone(stone)
                        domino_snake.append(stone)
                        input_checked = True
                    else:
                        continue
            except ValueError:
                continue
            except IndexError:
                continue
    elif turn == 'player':
        turn = 'computer'
        input_checked = False
        print('Status: It\'s your turn to make a move. Enter your command.')
        while not input_checked:
            try:
                move = int(input())
                stone = player_pieces[abs(move) - 1]
                if move < 0:
                    if check_move(stone, 'left'):
                        player_pieces.remove(stone)
                        if domino_snake[0][0] != stone[1]:
                            stone = reorient_stone(stone)
                        domino_snake.insert(0, stone)
                        input_checked = True
                    else:
                        print('Illegal move. Please try again.')
                        continue
                elif move == 0:
                    if len(stock_pieces):
                        stone = random.choice(stock_pieces)
                        stock_pieces.remove(stone)
                        player_pieces.append(stone)
                    input_checked = True
                elif move > 0:
                    if check_move(stone, 'right'):
                        player_pieces.remove(stone)
                        if domino_snake[-1][1] != stone[0]:
                            stone = reorient_stone(stone)
                        domino_snake.append(stone)
                        input_checked = True
                    else:
                        print('Illegal move. Please try again.')
                        continue
            except ValueError:
                print("Invalid input. Please try again.")
            except IndexError:
                print("Invalid input. Please try again.")

print(status)
