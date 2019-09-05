budget = int(input())
season = input()
fishermen_count = int(input())
boat_price = 0

if season == 'Spring':
    boat_price = 3000
    if fishermen_count <= 6:
        boat_price -= boat_price * 0.10
    elif fishermen_count <= 11:
        boat_price -= boat_price * 0.15
    else:
        boat_price -= boat_price * 0.25
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
    if fishermen_count <= 6:
        boat_price -= boat_price * 0.10
        # boat_price *= 0.9
    elif fishermen_count <= 11:
        boat_price -= boat_price * 0.15
    else:
        boat_price -= boat_price * 0.25
elif season == 'Winter':
    boat_price = 2600
    if fishermen_count <= 6:
        boat_price -= boat_price * 0.10
    elif fishermen_count <= 11:
        boat_price -= boat_price * 0.15
    else:
        boat_price -= boat_price * 0.25

if fishermen_count % 2 == 0 and not season == 'Autumn':
    boat_price -= boat_price * 0.05

if budget >= boat_price:
    print(f'Yes! You have {budget - boat_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {boat_price - budget:.2f} leva.')

