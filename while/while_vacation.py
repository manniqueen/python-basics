needed_money = float(input())
owned_money = float(input())

days_counter = 0
spend_counter =0

while owned_money < needed_money:
    action = input()
    sum = float(input())

    days_counter += 1

    if action == 'save':
        spend_counter = 0
        owned_money += sum
    elif action == 'spend':
        spend_counter += 1
        owned_money -= sum
        if owned_money < 0:
            owned_money = 0

    if spend_counter == 5:
        print(f"You can't save the money.")
        print(f'{days_counter}')
        break

if owned_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')