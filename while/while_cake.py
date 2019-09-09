import math

width = int(input())
length = int(input())
command = input()

all_pieces = width * length

while command != 'STOP':
    piece = int(command)
    all_pieces -= piece

    if all_pieces < 0:
        print(f'No more cake left! You need %d pieces more.' % math.fabs(all_pieces))
        break

    command = input()

if command == 'STOP':
    print(f'{all_pieces} pieces are left.')
