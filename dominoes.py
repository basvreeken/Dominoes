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
        print(f'{snake[0]}, {snake[1]}, {snake[2]}...{snake[-1]}, {snake[-2]},'
              f' {snake[-3]}')


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
        turn = 'player'
        domino_snake.append(max(player_doubles))
        player_pieces.remove(max(player_doubles))
        break
    elif len(player_doubles) == 0:
        turn = 'computer'
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
        input('Status: Computer is about to make a move. Press Enter to '
              'continue...\n')
        option = random.randint(0, 2)  # The test fails on grabbing a stone
        stone = random.choice(computer_pieces)
        if option == 0:
            stone = random.choice(stock_pieces)
            stock_pieces.remove(stone)
            computer_pieces.append(stone)
        elif option == 1:
            domino_snake.insert(0, stone)
            computer_pieces.remove(stone)
        elif option == 2:
            domino_snake.append(stone)
            computer_pieces.remove(stone)
    elif turn == 'player':
        turn = 'computer'
        input_checked = False
        print('Status: It\'s your turn to make a move. Enter your command.\n')
        while not input_checked:
            try:
                move = int(input())
                stone = player_pieces[abs(move) - 1]
                if move < 0:
                    domino_snake.insert(0, stone)
                    player_pieces.remove(stone)
                    input_checked = True
                elif move == 0:
                    stone = random.choice(stock_pieces)
                    stock_pieces.remove(stone)
                    player_pieces.append(stone)
                    input_checked = True
                elif move > 0:
                    domino_snake.append(stone)
                    player_pieces.remove(stone)
                    input_checked = True
            except ValueError:
                print("Invalid input. Please try again.")
            except IndexError:
                print("Invalid input. Please try again.")

print(status)
