budget = float(input())
season = input()

destination = None
price = None
type = None

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
     price = budget * 0.3
     type = 'Camp'
    elif season == 'winter':
        price = budget * 0.70
        type = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        type = 'Camp'
    elif season == 'winter':
        price = budget * 0.80
        type = 'Hotel'
else:
    destination = 'Europe'
    price = budget * 0.90
    type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type} - {price:.2f}')
