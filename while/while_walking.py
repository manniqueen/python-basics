goal = 10000
steps = 0

while steps < goal:
    command = input()
    if not command == 'Going home':
        steps += int(command)
    else:
        extra_steps= int(input())
        steps += extra_steps
        if steps >= goal:
            print(f'Goal reached! Good job!')
        else:
            print(f'{goal - steps} more steps to reach goal.')
            break

    if steps >= goal and command != 'Going home':
        print(f'Goal reached! Good job!')