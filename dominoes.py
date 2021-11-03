import random

domino_set = []
for i in range(0, 7):
    for j in range(i, 7):
        domino_set.append([i, j])

domino_snake = []
status = None

while not status:
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
        status = 'player'
        domino_snake.append(max(player_doubles))
        player_pieces.remove(max(player_doubles))
        break
    elif len(player_doubles) == 0:
        status = 'computer'
        domino_snake.append(max(computer_doubles))
        computer_pieces.remove(max(computer_doubles))
        break
    if max(computer_doubles) > max(player_doubles):
        status = 'player'
        domino_snake.append(max(computer_doubles))
        computer_pieces.remove(max(computer_doubles))
    else:
        status = 'computer'
        domino_snake.append(max(player_doubles))
        player_pieces.remove(max(player_doubles))

print('======================================================================')
print('Stock size: ' + str(len(stock_pieces)))
print('Computer pieces: ' + str(len(computer_pieces)))
print(f'\n{domino_snake[0]}\n')
print('Your pieces:')
for i in range(len(player_pieces)):
    print(f'{i + 1}:{player_pieces[i]}')
if status == 'computer':
    message = 'Computer is about to make a move. Press Enter to continue...'
else:
    message = 'It\'s your turn to make a move. Enter your command.'
print('\nStatus: ' + message)
